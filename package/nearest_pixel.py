# For each pixel in the image, find the nearest pixel that matches the target color criteria and calculate distances
import numpy as np
def find_nearest_pixel_img(image_path, target_color_lower, target_color_upper):
    from PIL import Image
    # Load the image
    image = Image.open(image_path)
    image = image.convert('RGB')
    data = np.array(image)

    # Create a mask for target color pixels
    target_mask = np.all((data >= target_color_lower) & (data <= target_color_upper), axis=-1)

    # Get coordinates of target color pixels
    target_coords = np.argwhere(target_mask)
    target_colors = data[target_mask]

    nearest_pixels = {}
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            color = data[i, j]
            distances = np.sqrt(np.sum((target_colors - color) ** 2, axis=-1))
            nearest_index = np.unravel_index(np.argmin(distances), distances.shape)
            nearest_pixels[(i, j)] = tuple(target_coords[nearest_index])

    return nearest_pixels

# Using 2 pixel tuple lists instead of image paths
def find_nearest_pixel_array(color_array_1, color_array_2):
    nearest_pixels = {}
    for i in range(len(color_array_1)):
        color1 = np.array(color_array_1[i])
        distances = np.sqrt(np.sum((np.array(color_array_2) - color1) ** 2, axis=-1))
        nearest_index = np.argmin(distances)
        nearest_pixels[tuple(color1)] = tuple(color_array_2[nearest_index])
    return nearest_pixels