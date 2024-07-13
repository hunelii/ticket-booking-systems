import tkinter as tk
from tkinter import simpledialog

# Create a 20x5 matrix filled with empty seats
plane_seating = [['Seat' for _ in range(5)] for _ in range(20)]

# Set the aisle (hall) column (index 2) to 'Hall'
for row in plane_seating:
    row[2] = 'Hall'

# Initialize Tkinter
root = tk.Tk()
root.title("Plane Ticket Booking System")

# Create a frame for seating arrangement display
frame = tk.Frame(root)

# Function to update and display seating arrangement in GUI
def update_display():
    for i, row in enumerate(plane_seating):
        for j, seat in enumerate(row):
            if seat == 'Seat':
                tk.Label(frame, text='[ ]', padx=5, pady=5).grid(row=i, column=j)
            elif seat == 'Booked':
                tk.Label(frame, text='[X]', padx=5, pady=5).grid(row=i, column=j)
            elif seat == 'Hall':
                tk.Label(frame, text='---', padx=5, pady=5).grid(row=i, column=j)

# Function to handle booking a seat
def book_seat_gui():
    try:
        row = simpledialog.askinteger("Seat Booking", "Enter row number (1-20):", parent=root, minvalue=1, maxvalue=20) - 1
        col = simpledialog.askinteger("Seat Booking", "Enter column number (1-5):", parent=root, minvalue=1, maxvalue=5) - 1
        
        if row is not None and col is not None:
            if 0 <= row < 20 and 0 <= col < 5:
                if plane_seating[row][col] == 'Seat':
                    plane_seating[row][col] = 'Booked'
                    update_display()
                    tk.Label(root, text=f"Seat at row {row+1}, column {col+1} has been successfully booked.").pack()
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
book_button.pack(pady=10)

# Pack the frame for seating arrangement display
frame.pack(padx=10, pady=10)

# Initialize and display initial seating arrangement
update_display()

# Start the GUI main loop
root.mainloop()

print("Thank you for using the seat booking system.")
