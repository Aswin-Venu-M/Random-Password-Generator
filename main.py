import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password(length=12, include_special_chars=True, include_digits=True):
    chars = string.ascii_letters
    if include_special_chars:
        chars += string.punctuation
    if include_digits:
        chars += string.digits

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_password():
    length = int(length_var.get())
    include_special_chars = special_chars_var.get()
    include_digits = digits_var.get()

    password = generate_random_password(length, include_special_chars, include_digits)
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Password copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")


length_var = tk.StringVar(value="12")
special_chars_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
password_var = tk.StringVar(value="")


length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root, textvariable=length_var)
special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)

generated_password_label = tk.Label(root, text="Generated Password:")
generated_password_display = tk.Label(root, textvariable=password_var)


length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry.grid(row=0, column=1, padx=10, pady=5)
special_chars_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
digits_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
generated_password_label.grid(row=5, column=0, padx=10, pady=5)
generated_password_display.grid(row=5, column=1, padx=10, pady=5)


root.mainloop()
