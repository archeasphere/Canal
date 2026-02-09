from PIL import Image
import numpy as np
from edgedetect import find_blue_edge_pixels, find_red_edge_pixels
from nearest_pixel import find_nearest_pixel_array
from adjustededge import new_edge

if __name__ == "__main__":
    # Find blue edge pixels
    blue_edges = find_blue_edge_pixels("Example.png")

    # Create an image to display only the blue edges
    blue_edge_image = Image.new('RGB', (1152, 684), color='white')
    for coord in blue_edges:
        blue_edge_image.putpixel((coord[1], coord[0]), (0, 0, 255))  # Note: coord is (row, col)

    blue_edge_image.show()

    # unsplit = True
    # first = blue_edges[0]
    # blue_edges.remove(first)
    # #if i is next to first, then split, else keep going until next to first
    # while unsplit == True:
    #     for i in blue_edges:
    #         if i[0] == first[0] + 1 or i[0] == first[0] - 1 or i[1] == first[1] + 1 or i[1] == first[1] - 1:
    #             first = i
    #             blue_edges.remove(i)
    #             break
    #     else:
    #         unsplit = False



    
    # Find red edge pixels
    red_edges = find_red_edge_pixels("Example.png")

    # Create an image to display only the red edges
    red_edge_image = Image.new('RGB', (1152, 684), color='white')
    for coord in red_edges:
        red_edge_image.putpixel((coord[1], coord[0]), (255, 0, 0))  # Note: coord is (row, col)

    red_edge_image.show()

    # display nearest pixel mappings between blue and red edge pixels
    nearest_mappings = find_nearest_pixel_array(blue_edges, red_edges)
    map_edge_image = Image.new('RGB', (1152, 684), color='white')
    for blue_pixel, red_pixel in nearest_mappings.items():
        map_edge_image.putpixel((blue_pixel[1], blue_pixel[0]), (0, 0, 255))  # Note: coord is (row, col)
        map_edge_image.putpixel((red_pixel[1], red_pixel[0]), (255, 0, 0))  # Note: coord is (row, col)
    map_edge_image.show()

    # Calculate total distance between blue and red edge pixels
    final_image = Image.new('RGB', (1152, 684), color='white')
    final_image_edges = []
    total_distance = 0
    total_pixels = len(nearest_mappings)
    for blue_pixel, red_pixel in nearest_mappings.items():
        blue_x = blue_pixel[1] - red_pixel[1]
        blue_y = blue_pixel[0] - red_pixel[0]
        distance = np.sqrt(blue_x**2 + blue_y**2)
        total_distance += distance
    average_distance = total_distance / total_pixels if total_pixels > 0 else 0
    # for blue_pixel, blue_pixel2 in nearest_mappings.items():
    #     final_image.putpixel(new_edge(blue_pixel, red_pixel, average_distance)(0, 255, 0))
    print(f"Average distance between blue and red edge pixels: {average_distance:.2f}")