#Calculate the distance between edge pixels of specific colors in an image
from PIL import Image
import numpy as np

def find_lengths(color_array_1, color_array_2):
    lengths = {}
    for i in range(len(color_array_1)):
        color1 = np.array(color_array_1[i])
        for j in range(len(color_array_2)):
            color2 = np.array(color_array_2[j])
            distance = np.sqrt(np.sum((color2 - color1) ** 2))
            lengths[(tuple(color1), tuple(color2))] = distance
    return lengths

def new_edge(river_side_1, river_side_2):
    
    new_edges = {}
    