import torch
import torch.nn as nn
import torch.nn.functional as F
import AlgoTradeDataSet as ds
import torchvision
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
import os

MODEL = "algotrade3.pt"
BATCH_SIZE = 1
IMAGE_SIZE = ds.IMAGE_SIZE         # MUST MATCH MODEL


test = ds.StockDataset(root_dir='\\CoinCurrent', transform=transforms.Compose([
    transforms.ToPILImage(),
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5]),
]))
testloader = DataLoader(test, batch_size=BATCH_SIZE, shuffle=False)

files = []
for file in os.listdir(os.getcwd() + "\\CoinCurrent"):
    if file.endswith('.png'):
        files.append(str(file))


if torch.cuda.is_available():
    device = torch.device("cuda:0")
    print(torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")

net = torchvision.models.resnet152(pretrained=False).to(device)

net.load_state_dict(torch.load("inferenceDAYTRADE.pt"))

classes = ("Fall", "Stable", "Rise")

correct = 0

net = net.eval()
criterion = nn.CrossEntropyLoss()
i = 0
for data in testloader:
    images, labels = data.get("image").to(device), data.get("solution").to(device)
    outputs = net(images)
    _, predicted = torch.max(outputs.data, 1)
    if predicted == torch.tensor([750]).to(device):
        probabilities = F.softmax(outputs, dim=1)
        if probabilities[0][750] > 0.7:
            print(probabilities[0][750])
            print(files[i])
    i += 1