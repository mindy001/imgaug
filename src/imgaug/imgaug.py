import struct

def read_image(image_path):
    """Reads an image and returns the pixel data as a list of lists (rows and columns)."""
    with open(image_path, 'rb') as f:
        header = f.read(18) 
        width, height = struct.unpack('ii', header[12:18])  
        f.seek(18)
        image_data = f.read()
    

    return width, height, image_data

def display_image(width, height, image_data):
    """Displays the image by printing out pixel values (basic ASCII art)."""
    for i in range(height):
        for j in range(width):
            pixel = image_data[i * width + j]
            print(f"{pixel:02x}", end=" ")
        print()  

def rotate_90_degrees(width, height, image_data):
    """Rotates the image 90 degrees clockwise."""
    new_width = height
    new_height = width
    new_image_data = [0] * (new_width * new_height)
    
    for i in range(width):
        for j in range(height):
            new_image_data[j * new_width + (new_width - 1 - i)] = image_data[i * height + j]
    
    return new_width, new_height, new_image_data

def rotate_180_degrees(width, height, image_data):
    """Rotates the image 180 degrees (flip it upside down)."""
    new_image_data = [0] * (width * height)
    
    for i in range(width):
        for j in range(height):
            new_image_data[(height - 1 - j) * width + (width - 1 - i)] = image_data[i * height + j]
    
    return width, height, new_image_data

def make_square_image(width, height, image_data):
    """Makes the image square by resizing the smaller dimension to match the larger one."""
    new_size = max(width, height)
    new_image_data = [0] * (new_size * new_size)
    
    for i in range(width):
        for j in range(height):
            new_image_data[j * new_size + i] = image_data[i * height + j]
    
    return new_size, new_size, new_image_data