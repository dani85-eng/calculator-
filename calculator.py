import tkinter as tk
from tkinter import messagebox
import math

# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    if x < 0:
        return "Error! Square root of a negative number."
    else:
        return math.sqrt(x)

# Function to perform the chosen operation
def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    if operation.get() == 'Add':
        result = add(num1, num2)
    elif operation.get() == 'Subtract':
        result = subtract(num1, num2)
    elif operation.get() == 'Multiply':
        result = multiply(num1, num2)
    elif operation.get() == 'Divide':
        result = divide(num1, num2)
    elif operation.get() == 'Power':
        result = power(num1, num2)
    elif operation.get() == 'Square Root':
        result = sqrt(num1)
        entry_num2.delete(0, tk.END)  # Clear second number entry for square root operation
    else:
        result = "Invalid operation"

    if isinstance(result, str):
        messagebox.showerror("Error", result)
    else:
        label_result.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

entry_num1.grid(row=0, column=1, padx=10, pady=10)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

operation = tk.StringVar(value='Add')

tk.Radiobutton(root, text="Add", variable=operation, value='Add').grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Subtract", variable=operation, value='Subtract').grid(row=2, column=1, padx=10, pady=10)
tk.Radiobutton(root, text="Multiply", variable=operation, value='Multiply').grid(row=2, column=2, padx=10, pady=10)
tk.Radiobutton(root, text="Divide", variable=operation, value='Divide').grid(row=2, column=3, padx=10, pady=10)
tk.Radiobutton(root, text="Power", variable=operation, value='Power').grid(row=3, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Square Root", variable=operation, value='Square Root').grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate", command=perform_operation).grid(row=4, column=0, columnspan=4, padx=10, pady=10)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
