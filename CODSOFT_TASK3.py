import tkinter as tk
import random
import string

def generate_password(length, complexity):
    password = ''
    if complexity == 'Low':
        characters = string.ascii_lowercase
    elif complexity == 'Medium':
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length):
        password += random.choice(characters)

    return password

def generate_password_gui():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    password_label.config(text="Your generated password is: " + password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Length entry
length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Complexity dropdown
complexity_label = tk.Label(root, text="Choose the complexity of the password:")
complexity_label.grid(row=1, column=0, padx=10, pady=5)
complexity_var = tk.StringVar(root)
complexity_choices = ['Low', 'Medium', 'High']
complexity_var.set('Low')  # Default value
complexity_menu = tk.OptionMenu(root, complexity_var, *complexity_choices)
complexity_menu.grid(row=1, column=1, padx=10, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Generated password label
password_label = tk.Label(root, text="")
password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()