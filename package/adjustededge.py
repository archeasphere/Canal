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

#Takes the coordiantes of the two river sides and the length to adjust by, and returns the new edge coordinates after adding the length in line with the nearest pixel on the opposite river side
def new_edge(river_side_1, river_side_2, length):
    new_edge = {}
    #find the angle between the two river sides
    for i in range(len(river_side_1)):
        color1 = np.array(river_side_1[i])
        nearest_color2 = None
        nearest_distance = float('inf')
        for j in range(len(river_side_2)):
            color2 = np.array(river_side_2[j])
            distance = np.sqrt(np.sum((color2 - color1) ** 2))
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_color2 = color2
        #calculate the angle between the two colors
        angle = np.arctan2(nearest_color2[1] - color1[1], nearest_color2[0] - color1[0])
        #calculate the new edge coordinates by adding the length in line with the angle
        new_x = int(color1[0] + length * np.cos(angle))
        new_y = int(color1[1] + length * np.sin(angle))
        new_edge[tuple(color1)] = (new_x, new_y)
    return new_edge
    