import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        # Retrieves and convert inputs to float
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        # Performs the selected operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result_label.config(text="Error: Division by zero")
                return
        else:
            result_label.config(text="Invalid Operation")
            return

        # Updates the result label
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers")

# Sets up the main window
root = tk.Tk()
root.title("B\'s Simple Calculator")

# Number 1 input
label_num1 = ttk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5, sticky='E')
entry_num1 = ttk.Entry(root)
entry_num1.grid(row=0, column=1,padx=5, pady=5)

# Number 2 input
label_num2 = ttk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5, sticky='E')
entry_num2 = ttk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Operation Selection
label_operation = ttk.Label(root, text="Operation:")
label_operation.grid(row=2, column=0, padx=5, pady=5, sticky='E')

operations = ['+', '-', '*', '/']
combo_operation = ttk.Combobox(root, values=operations, state="readonly")
combo_operation.grid(row=2, column=1, padx=5, pady=5)
combo_operation.current(0) # Default to addition

# Calculate button
calc_button = ttk.Button(root, text="Calculate", command = calculate)
calc_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Result Display
result_label = ttk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the application
root.mainloop()
