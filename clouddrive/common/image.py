from PIL import Image
import os
import clouddrive.common.tinify as tinify

# Set your TinyPNG/TinyJPG API key
tinify.key = "XYJdM1h6R0HSVS00qkTZsVVKtL6xfkmq"

def compress_image(filepath, quality=50):
            if filepath.endswith(".jpg") or filepath.endswith(".jpeg"):
                try:
                    img = Image.open(filepath)
                    img = img.convert('RGB')
                    img.save(filepath, optimize=True, quality=quality)
                    print(f"Compression successful: {filepath}")
                except Exception as e:
                    print(f"Compression failed: {filepath} - {str(e)}")
            elif filepath.endswith(".png"):
                try:
                    source = tinify.from_file(filepath)
                    source.to_file(filepath)
                    print(f"Compression successful: {filepath}")
                except tinify.Error as e:
                    print(f"Compression failed: {filepath} - {str(e)}")

def compress_images(directory, quality=50):
    if os.path.isdir(directory):
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                compress_image(filepath, quality)
    elif os.path.isfile(directory):
        compress_image(directory, quality)
    else:
        print("Invalid path")


