from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

IMAGE_SIZE = 70
BATCH_SIZE = 64


# A set of the stock data, lol
class StockDataset(Dataset):
    def __init__(self, root_dir, transform=None):

        self.root_dir = os.getcwd() + root_dir
        self.files = []
        for file in os.listdir(self.root_dir):
            if file.endswith('.png'):
                self.files.append(str(file));

        self.transform = transform

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = self.files[idx]

        if img_name.split(".")[0] == "rise":
            self.solution = 750;
        else:
            self.solution = 250;
        img_name = self.root_dir + "\\" + img_name

        image = io.imread(img_name)

        sample = {"image": image, "solution": self.solution}

        if self.transform:
            sample['image'] = self.transform(sample['image'])

        return sample


# Apply each of the above transforms on sample.
transformed_dataset = StockDataset(root_dir='\\TrainingSet5', transform=transforms.Compose([
    transforms.ToPILImage(),
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5]),
]))

# for i in range(len(transformed_dataset)):
#    sample = transformed_dataset[i]
#
#    print(i, sample['image'].size(), sample['solution'])
#
#    if i == 3:
#        break

dataloader = DataLoader(transformed_dataset, batch_size=BATCH_SIZE, pin_memory=True,
                        shuffle=True, num_workers=0)
