from PIL import Image, ImageDraw

x=347
y=221
def draw_cross_on_square(input_path, output_path, center, square_size, x_color=(255, 0, 0), x_thickness=5):
    cx, cy = center
    half_size = square_size // 2
    
    # Calculate the corners of the square
    top_left = (cx - half_size, cy - half_size)
    top_right = (cx + half_size, cy - half_size)
    bottom_left = (cx - half_size, cy + half_size)
    bottom_right = (cx + half_size, cy + half_size)

    # Open an image file
    with Image.open(input_path) as im:
        # Create a drawing object
        draw = ImageDraw.Draw(im)
        
        # Draw the diagonals
        draw.line([top_left, bottom_right], fill=x_color, width=x_thickness)
        draw.line([top_right, bottom_left], fill=x_color, width=x_thickness)
        
        # Save the image with the X drawn on it
        im.save(output_path)

# Example usage with two squares
draw_cross_on_square(
    'input.png',  # input image path
    'output.png',  # output image path
    center=(x, y),  # center of the first square
    square_size=25,  # size of the first square
    x_color=(255, 0, 0),  # color of the first cross (red)
    x_thickness=5  # thickness of the first cross
)

# Draw a cross on another square
draw_cross_on_square(
    'output.png',  # input image path (use output of the first function call)
    'output.png',  # output image path (overwrite the same image)
    center=(x+33, y),  # center of the second square
    square_size=25,  # size of the second square
    x_color=(0, 255, 0),  # color of the second cross (green)
    x_thickness=5  # thickness of the second cross
)
draw_cross_on_square(
    'output.png',  # input image path (use output of the first function call)
    'output.png',  # output image path (overwrite the same image)
    center=(x, y+33),  # center of the second square
    square_size=25,  # size of the second square
    x_color=(0, 0, 255),  # color of the second cross (green)
    x_thickness=5  # thickness of the second cross
)
