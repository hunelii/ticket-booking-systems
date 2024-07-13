import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize the seating plan based on the given layout
plane_seating = [
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
    ['Seat', 'Seat', 'Seat', 'Seat', 'Seat'],
]

# Initialize Tkinter
root = tk.Tk()
root.title("Plane Ticket Booking System")

# Create a frame for seating arrangement display
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Function to update and display seating arrangement in GUI
def update_display():
    for widget in frame.winfo_children():
        widget.destroy()
    for i, row in enumerate(plane_seating):
        for j, seat in enumerate(row):
            if seat == 'Seat':
                tk.Label(frame, text='[ ]', padx=5, pady=5).grid(row=i, column=j)
            elif seat == 'Booked':
                tk.Label(frame, text='[X]', padx=5, pady=5).grid(row=i, column=j)

# Function to handle booking a seat
def book_seat_gui():
    try:
        row = simpledialog.askinteger("Seat Booking", "Enter row number (1-35):", parent=root, minvalue=1, maxvalue=35) - 1
        col = simpledialog.askinteger("Seat Booking", "Enter column number (1-5):", parent=root, minvalue=1, maxvalue=5) - 1
        
        if row is not None and col is not None:
            if 0 <= row < 35 and 0 <= col < 5:
                if plane_seating[row][col] == 'Seat':
                    plane_seating[row][col] = 'Booked'
                    update_display()
                    messagebox.showinfo("Success", f"Seat at row {row+1}, column {col+1} has been successfully booked.")
                else:
                    messagebox.showerror("Error", "Seat is already booked. Please choose another seat.")
            else:
                messagebox.showerror("Error", "Invalid row or column number. Please enter valid numbers.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid row and column numbers.")

# Button to book a seat
book_button = tk.Button(root, text="Book Seat", command=book_seat_gui)
book_button.pack()

# Initialize and display initial seating arrangement
update_display()

# Start the GUI main loop
root.mainloop()

print("Thank you for using the seat booking system.")
