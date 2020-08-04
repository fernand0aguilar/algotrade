import torch
import torch.nn as nn
import torch.nn.functional as F
import AlgoTradeDataSet as ds
import torchvision
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader

BATCH_SIZE = 1
IMAGE_SIZE = ds.IMAGE_SIZE         # MUST MATCH MODEL


test = ds.StockDataset(root_dir='\\ValidationSet5', transform=transforms.Compose([
    transforms.ToPILImage(),
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5]),
]))
testloader = DataLoader(test, batch_size=BATCH_SIZE, shuffle=False)

if torch.cuda.is_available():
    device = torch.device("cuda:0")
    print(torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")

net = torchvision.models.resnet152(pretrained=False).to(device)

net.load_state_dict(torch.load("inferenceDAYTRADE5.pt"))

classes = ("Fall", "Stable", "Rise")

correct = 0
stable_total = 0
stable_right = 0
fall_right = 0
fall_total = 0
rise_right = 0
rise_total = 0
total = 0
true_error = 0
rise_calculated = 0

net = net.eval()
criterion = nn.CrossEntropyLoss()

for data in testloader:
    images, labels = data.get("image").to(device), data.get("solution").to(device)
    outputs = net(images)
    _, predicted = torch.max(outputs.data, 1)
    total += labels.size(0)
    print(criterion(outputs, labels))
    correct += (predicted == labels).sum().item()
    probabilities = F.softmax(outputs, dim=1)
    print(predicted)
    if labels == torch.tensor([250]).to(device):
        if predicted == labels:
            fall_right +=1
            print("fall")
        fall_total +=1
    if labels == torch.tensor([500]).to(device):
        if predicted == labels:
            stable_right +=1
            print("stable")
        stable_total +=1
    if labels == torch.tensor([750]).to(device):
        if predicted == labels:
            rise_right +=1
            if probabilities[0][750] > 0.51:
                rise_calculated += 1
            print("rise")
        rise_total +=1
    if labels != torch.tensor([750]).to(device) and probabilities[0][750] > 0.51:
        true_error +=1

print('Accuracy of the network on the test images: %d %%' % (
        100 * correct / total))
print('Accuracy of the network by class on test images:')
print('Accuracy of Rise: ', (
        100 * rise_right / rise_total), "%")
print('Accuracy of Fall: ', (
        100 * fall_right / fall_total), "%")
print('TRUE ERRORS: ', true_error)

print("TOTAL RISES AVAILABLE", rise_calculated)