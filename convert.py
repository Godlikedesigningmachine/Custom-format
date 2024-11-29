from PIL import Image
import struct
import sys

def convert_png_to_custom(png_path, custom_path):
    try:
        # Open the image and get its size and pixels
        image = Image.open(png_path)
        width, height = image.size
        pixels = list(image.getdata())

        # Write the custom format file
        with open(custom_path, 'wb') as file:
            file.write(f"{width} {height}\n".encode('utf-8'))

            # Convert pixel data to RGB and write to file
            for pixel in pixels:
                r, g, b = pixel[:3]
                file.write(struct.pack('3B', r, g, b))

        print(f"Conversion successful: {png_path} -> {custom_path}")
        return True
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False

def main(original_path, custom_path):
    print(f"Found Image at {original_path}")
    print(f"Converting to {custom_path}")
    success = convert_png_to_custom(original_path, custom_path)
    if success:
        print("Conversion Complete.")
    else:
        print("Failed to convert due to some error.")
    return success

def validate_args(args):
    if len(args) < 3:
        print("Usage: python script.py <original_path> <custom_path>")
        return False
    return True

if __name__ == "__main__":
    if not validate_args(sys.argv):
        sys.exit(1)

    original_path = sys.argv[1]
    custom_path = sys.argv[2]

    main(original_path, custom_path)
