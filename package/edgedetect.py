#identify all blue edge pixels in an image and create a list of their coordinates using numpy and PIL
from PIL import Image
import numpy as np
def find_blue_edge_pixels(image_path):
    # Load the image
    image = Image.open(image_path)
    image = image.convert('RGB')
    data = np.array(image)

    # Define blue color range
    lower_blue = np.array([0, 0, 100])
    upper_blue = np.array([100, 100, 255])

    # Create a mask for blue pixels
    blue_mask = np.all((data >= lower_blue) & (data <= upper_blue), axis=-1)

    # Find edge pixels using a simple gradient method
    edges = np.zeros(blue_mask.shape, dtype=bool)
    edges[1:-1, 1:-1] = (
        (blue_mask[1:-1, 1:-1] != blue_mask[:-2, 1:-1]) |
        (blue_mask[1:-1, 1:-1] != blue_mask[2:, 1:-1]) |
        (blue_mask[1:-1, 1:-1] != blue_mask[1:-1, :-2]) |
        (blue_mask[1:-1, 1:-1] != blue_mask[1:-1, 2:])
    )

    # Get coordinates of blue edge pixels
    blue_edge_coords = np.argwhere(edges & blue_mask)

    # Convert to list of tuples
    blue_edge_list = [tuple(coord) for coord in blue_edge_coords]

    return blue_edge_list

def find_red_edge_pixels(image_path):
    # Load the image
    image = Image.open(image_path)
    image = image.convert('RGB')
    data = np.array(image)

    # Define red color range
    lower_red = np.array([100, 0, 0])
    upper_red = np.array([255, 100, 100])

    # Create a mask for red pixels
    red_mask = np.all((data >= lower_red) & (data <= upper_red), axis=-1)

    # Find edge pixels using a simple gradient method
    edges = np.zeros(red_mask.shape, dtype=bool)
    edges[1:-1, 1:-1] = (
        (red_mask[1:-1, 1:-1] != red_mask[:-2, 1:-1]) |
        (red_mask[1:-1, 1:-1] != red_mask[2:, 1:-1]) |
        (red_mask[1:-1, 1:-1] != red_mask[1:-1, :-2]) |
        (red_mask[1:-1, 1:-1] != red_mask[1:-1, 2:])
    )

    # Get coordinates of red edge pixels
    red_edge_coords = np.argwhere(edges & red_mask)

    # Convert to list of tuples
    red_edge_list = [tuple(coord) for coord in red_edge_coords]

    return red_edge_list

def find_split_blue_edge_pixels(image_path):
    # Load the image
    image = Image.open(image_path)
    image = image.convert('RGB')
    data = np.array(image)

    # Define blue color range
    lower_blue = np.array([0, 0, 100])
    upper_blue = np.array([100, 100, 255])

    # Create a mask for blue pixels
    blue_mask = np.all((data >= lower_blue) & (data <= upper_blue), axis=-1)

    # Find edge pixels using a simple gradient method
    edges = np.zeros(blue_mask.shape, dtype=bool)
    edges[1:-1, 1:-1] = (
        (blue_mask[1:-1, 1:-1] != blue_mask[:-2, 1:-1]) |
        (blue_mask[1:-1, 1:-1] != blue_mask[2:, 1:-1]) |
        (blue_mask[1:-1, 1:-1] != blue_mask[1:-1, :-2]) |
        (blue_mask[1:-1, 1:-1] != blue_mask[1:-1, 2:])
    )

    # Get coordinates of blue edge pixels
    blue_edge_coords = np.argwhere(edges & blue_mask)

    # Split the edge pixels into two lines by detecting their neearest blue pixel
    mid_row = data.shape[0] // 2
    upper_line_coords = blue_edge_coords[blue_edge_coords[:, 0] < mid_row]
    lower_line_coords = blue_edge_coords[blue_edge_coords[:, 0] >= mid_row]
    blue_edge_coords = np.vstack((upper_line_coords, lower_line_coords))

    # Convert to list of tuples
    blue_edge_list = [tuple(coord) for coord in blue_edge_coords]

    return blue_edge_list