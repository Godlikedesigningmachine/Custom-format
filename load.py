import pygame
import sys
from PIL import Image
import struct

# Define a class for Pixel
class Pixel:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getRGB(self):
        return (self.r, self.g, self.b)

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

# Function to load a custom image
def load_custom_image(custom_path):
    pixels = []

    try:
        with open(custom_path, 'rb') as file:
            # Read and decode the first line to get width and height
            first_line = file.readline().decode('utf-8').strip()
            width, height = map(int, first_line.split())

            # Read the rest of the pixel data
            pixel_data = file.read()
            pixel_count = width * height

            # Check if the file has enough pixel data
            if len(pixel_data) < pixel_count * 3:
                raise ValueError("Not enough pixel data in the file")

            # Parse pixel data
            index = 0
            for i in range(height):
                row = []
                for j in range(width):
                    r, g, b = struct.unpack_from('3B', pixel_data, index)
                    index += 3
                    row.append(Pixel(r, g, b))
                pixels.append(row)
        
        print(f"Loaded custom image with dimensions: {width}x{height}")
        return pixels, width, height
    except Exception as e:
        print(f"Error loading custom image: {e}")
        raise

def initialize_pygame_window(width, height):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Custom Image Viewer')
    print("Initialized Pygame window.")
    return window

def draw_image(window, pixels, width, height):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the window with white color
        window.fill((255, 255, 255))

        # Draw the pixels on the window
        for y, row in enumerate(pixels):
            for x, pixel in enumerate(row):
                pygame.draw.rect(window, pixel.getRGB(), (x, y, 1, 1))

        pygame.display.flip()

    pygame.quit()
    print("Pygame window closed.")
    sys.exit()

def main(image_path):
    try:
        pixels, width, height = load_custom_image(image_path)
    except Exception as e:
        print(f"Error loading custom image: {e}")
        sys.exit(1)

    window = initialize_pygame_window(width, height)
    draw_image(window, pixels, width, height)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <custom_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    main(image_path)
