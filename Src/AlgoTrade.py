import os

import torch
import torchvision
from torch import optim
import torch.utils.data
import torch.nn as nn
import torch.nn.functional as F
import AlgoTradeDataSet as ds

MODEL = "algotradeDAYTRADE15.pt"

BATCH_SIZE = ds.BATCH_SIZE

IMAGE_SIZE = ds.IMAGE_SIZE

train = ds.transformed_dataset
trainset = ds.dataloader

if torch.cuda.is_available():
    device = torch.device("cuda:0")
    print(torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=5, stride=1, padding=2)
        self.conv2 = nn.Conv2d(9, 81, kernel_size=3)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc6 = nn.Linear(81 * 33 * 33, 34 * 34)
        self.fc7 = nn.Linear(34*34, 64)
        self.fc8 = nn.Linear(64, 4)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.pool(x))
        x = x.view(x.shape[0], -1)
        x = F.relu(self.fc6(x))
        x = F.relu(self.fc7(x))

        return self.fc8(x)


model = torchvision.models.resnet152(pretrained=False).to(device)
# model = torch.load(MODEL).to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()
EPOCHS = 50
net = model.train()
for epoch in range(EPOCHS):
    print("Epoch = ", epoch)
    i = 0
    cum_loss = 0
    total_train = 0
    correct_train = 0
    for data in trainset:
        X = data.get("image").to(device)
        y = data.get("solution").to(device)
        optimizer.zero_grad()
        output = model(X)
        loss = criterion(output, y.long())
        loss.backward()
        optimizer.step()
        i += BATCH_SIZE
        cum_loss += loss
        _, prediction = torch.max(output.data, 1)
        print(loss)
        print(i)
        total_train += y.nelement()
        correct_train += prediction.eq(y.data).sum().item()
        train_accuracy = 100 * correct_train / total_train
    print("Accuracy = ",train_accuracy, "%")

    torch.save(model, 'algotradeDAYTRADE5.pt')
    torch.save(model.state_dict(), "inferenceDAYTRADE5.pt")
    print(f"Total Loss: {cum_loss/len(trainset)}")
