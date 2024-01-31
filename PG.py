import tkinter as tk
import random
import string

def generate_password():
    length = int(length_var.get())

    if length <= 0:
        result_var.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    if include_uppercase.get():
        characters += string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)

include_uppercase = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=include_uppercase)
uppercase_check.grid(row=1, columnspan=2, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), wraplength=300)
result_label.grid(row=3, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
