import tkinter as tk
from tkinter import ttk
import random
import string

# Main Window
root = tk.Tk()
root.title("Password Generator")

# Frame
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label and entry for password length
length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_length = ttk.Entry(frame, width=10)
entry_length.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Button to generate password
generate_button = ttk.Button(frame, text="Generate Password")
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Checkbutton to toggle the display of the password
show_password = tk.BooleanVar()
show_checkbox = ttk.Checkbutton(frame, text="Show Password", variable=show_password)
show_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Label to display the generated password(masked or unmasked)
result_label = ttk.Label(frame, text="Your Password will appear here")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

#Button to copy the password to clipboard
copy_button = ttk.Button(frame, text="Copy Password")
copy_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Label to show copy status message
copy_status_label = ttk.Label(frame, text="")
copy_status_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Global variable for generated password
generated_password = ""

def generate_password():
    global generated_password
    try:
        # Get the desired password length
        length = int(entry_length.get())
        if length < 4:
            result_label.config(text="You can only create password with 4 characters or more")    
            return
        
        # Pool of characters (letters, digits, punctuation)
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password
        generated_password = ''.join(random.choice(characters) for _ in range(length))

        # Display password based on checkbox state (masked or unmasked)
        if show_password.get():
            result_label.config(text=generated_password)
        else:
            result_label.config(text='*' * length)
    except ValueError:
        result_label.config(text="Error: Enter a valid integer")

def toggle_password():
    # Updates the display based on the checkbox state
    if show_password.get():
        result_label.config(text=generated_password)
    else:
        try:
            length = int(entry_length.get())
        except ValueError:
            length = len(generated_password)
        result_label.config(text='*' * length)

def copy_password():
    if generated_password:
        # clears the clipboard and copy the actual generated password
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        copy_status_label.config(text="Password copied to clipboard!")

        #clears the copy status message after 2 seconds
        root.after(2000, lambda: copy_status_label.config(text=""))
    else:
        copy_status_label.config(text="No Password to Copy!")
        root.after(2000, lambda: copy_status_label.config(text=""))

# Linking the buttons and checkbox to their functions
generate_button.config(command=generate_password)
show_checkbox.config(command=toggle_password)
copy_button.config(command=copy_password)

# Starts the event loop
root.mainloop()