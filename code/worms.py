import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torchvision.transforms as transforms
import os
from matplotlib import cm

def inverse_gaussian(x):
    return -1./torch.pow(2., (0.6*torch.pow(x, 2.)))+1.

class NCA(nn.Module):
    def __init__(self):
        super(NCA, self).__init__()
        self.kernel = torch.tensor([[[[ 0.68,  -0.9, 0.68],
          [-0.9, -0.66,  -0.9],
          [ 0.68, -0.9, 0.68]]]])
        
    def forward(self, x):
        return inverse_gaussian(nn.functional.conv2d(x, self.kernel, padding=1))
    
worms = NCA()

grid = torch.rand(1, 1, 512, 512)
for i in range(3000):
    grid = worms(grid)

grid = grid[0, 0].detach().numpy()


# Display the grid
plt.imshow(grid, cmap='copper')
plt.colorbar()
plt.show()
