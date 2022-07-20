import torch
from torch.utils.data import Dataset, DataLoader

class SimpleEuclideanDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, idx):
        data = self.data[idx]
        label = self.labels[idx]
        # sample = {"Data": data, "Class": label}
        sample = [data, label]
        return sample