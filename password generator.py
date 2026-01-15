import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid positive number for length."
        )
        return

    characters = ""

    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning(
            "Selection Error",
            "Please select at least one character type."
        )
        return

    # Supports long passwords (any length)
    password = "".join(random.choice(characters) for _ in range(length))

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# Main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Length input
tk.Label(root, text="Password Length:", font=("Arial", 11)).pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack()

# Character options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase Letters", variable=var_upper).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Lowercase Letters", variable=var_lower).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Numbers", variable=var_digits).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Symbols", variable=var_symbols).pack(anchor="w", padx=40)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result field
result_entry = tk.Entry(root, width=30, font=("Arial", 11))
result_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Run application
root.mainloop()
