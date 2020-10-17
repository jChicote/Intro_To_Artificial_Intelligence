import os
import torch
import pandas as pd
from torch.utils.data import Dataset
from skimage import io

class TestDataset(Dataset):
    def __init__(self, root, train=True, transform=None):
        self.train = train
        self.image_paths = glob.glob(path + '*.jpg')
        self.transform = transform

    def __getitem__(self, index):
        x = Image.open(self.image_paths[index])
        if self.transform is not None:
            x = self.transform(x)

        return x

    def __len__(self):
        return len(self.image_paths)