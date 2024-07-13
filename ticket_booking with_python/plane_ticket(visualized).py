from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import simpledialog
x_coo = None
y_coo = None
def calculate_coordinates(row, col):
    global x_coo, y_coo  # Declare x_coo and y_coo as global variables
    row_a=row*33
    y_coo = 221 + row_a
    
    if col == 0:
        x_coo = 347
    elif col == 1:
        x_coo = 380
    elif col == 3:
        x_coo = 443
    elif col == 5:
        x_coo = 475




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

# Create a 33x5 matrix filled with empty seats
plane_seating = [['Seat' for _ in range(5)] for _ in range(33)]

# Set the aisle (hall) column (index 2) to 'Hall'
for row in plane_seating:
    row[2] = 'Hall'

# Initialize Tkinter
root = tk.Tk()
root.title("Plane Ticket Booking System")

# Create a frame for seating arrangement display
frame = tk.Frame(root)

# Function to handle booking a seat
def book_seat_gui():
    try:
        row = simpledialog.askinteger("Seat Booking", "Enter row number (1-33):", parent=root, minvalue=1, maxvalue=33) - 1
        col = simpledialog.askinteger("Seat Booking", "Enter column number (1-5):", parent=root, minvalue=1, maxvalue=5) - 1
        calculate_coordinates(row, col)
        
        if row is not None and col is not None:
            if 0 <= row < 33 and 0 <= col < 5:
                if plane_seating[row][col] == 'Seat':
                    plane_seating[row][col] = 'Booked'
                    
                    # Calculate coordinates here again if necessary
                    calculate_coordinates(row, col)
                    """
                    print(row,col)
                    print(x_coo,y_coo)
                    """
                    draw_cross_on_square(
                        'output.png',  # input image path (use output of the first function call)
                        'output.png',  # output image path (overwrite the same image)
                        center=(x_coo, y_coo),  # center of the square
                        square_size=25,  # size of the square
                        x_color=(255, 0, 0),  # color of the cross
                        x_thickness=5  # thickness of the cross
                    )
                    update_image('output.png')

                    tk.Label(root, text=f"Seat at row {row+1}, column {col+1} has been successfully booked.").pack(pady=10)
                elif col == 2:
                    tk.Label(root, text="That is the corridor. Please choose another seat.").pack()
                else:
                    tk.Label(root, text="Seat is already booked. Please choose another seat.").pack()
            else:
                tk.Label(root, text="Invalid row or column number. Please enter valid numbers.").pack()
    except ValueError:
        tk.Label(root, text="Invalid input. Please enter valid row and column numbers.").pack()


# Button to book a seat
book_button = tk.Button(root, text="Book Seat", command=book_seat_gui)
book_button.pack(pady=10,padx=100)

image_label = tk.Label(root)
image_label.pack()
def update_image(image_path):
    img = Image.open('output.png')
    img = img.resize((405, 625), Image.LANCZOS)  # Resize image if necessary
    img = ImageTk.PhotoImage(img)
    
    # Update the image displayed in the label
    image_label.configure(image=img)
    image_label.image = img  # Keep reference to avoid garbage collection
update_image('output.png')


# Pack the frame for seating arrangement display
frame.pack(padx=10, pady=10)



# Start the GUI main loop
root.mainloop()

print("Thank you for using the seat booking system.")
