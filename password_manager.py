import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

def save_passwords():
    with open("passwords.txt", "w") as file:
        for (website, username), password in passwords.items():
            file.write(f"{website},{username},{password}\n")

def load_passwords():
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                website, username, password = line.strip().split(",")
                passwords[(website, username)] = password
    except FileNotFoundError:
        pass

def add_password():
    website = simpledialog.askstring("Add Password", "Enter website:")
    if website:
        username = simpledialog.askstring("Add Password", f"Enter username for {website}:")
        if username:
            password = simpledialog.askstring("Add Password", "Enter password:")
            if password:
                passwords[(website, username)] = password
                save_passwords()
                messagebox.showinfo("Success", "Password added successfully!")
            else:
                messagebox.showerror("Error", "Password cannot be empty!")
        else:
            messagebox.showerror("Error", "Username cannot be empty!")
    else:
        messagebox.showerror("Error", "Website cannot be empty!")

def remove_password():
    website = simpledialog.askstring("Remove Password", "Enter website:")
    if website:
        username = simpledialog.askstring("Remove Password", f"Enter username for {website}:")
        if (website, username) in passwords:
            del passwords[(website, username)]
            save_passwords()
            messagebox.showinfo("Success", "Password removed successfully!")
        else:
            messagebox.showerror("Error", "Password not found!")
    else:
        messagebox.showerror("Error", "Website cannot be empty!")

def view_passwords():
    key = simpledialog.askstring("View Passwords", "Enter security key:")
    if key == "VIDHI24":
        if passwords:
            password_info = "Saved Passwords:\n\n"
            for (website, username), password in passwords.items():
                password_info += f"Website: {website}\nUsername: {username}\nPassword: {password}\n\n"
            messagebox.showinfo("Password List", password_info)
        else:
            messagebox.showinfo("Password List", "No passwords saved yet.")
    else:
        messagebox.showerror("Error", "Invalid security key!")

def edit_password():
    website = simpledialog.askstring("Edit Password", "Enter website:")
    if website:
        username = simpledialog.askstring("Edit Password", f"Enter username for {website}:")
        if (website, username) in passwords:
            new_password = simpledialog.askstring("Edit Password", "Enter new password:")
            if new_password:
                passwords[(website, username)] = new_password
                save_passwords()
                messagebox.showinfo("Success", "Password updated successfully!")
            else:
                messagebox.showerror("Error", "Password cannot be empty!")
        else:
            messagebox.showerror("Error", "Password not found!")
    else:
        messagebox.showerror("Error", "Website cannot be empty!")

passwords = {}

load_passwords()

root = tk.Tk()
root.title("Your Personal Password Manager")

root.geometry("500x450")

heading_label = tk.Label(root, text="Password Manager", font=("Helvetica", 20), bg="light blue", fg="black")
heading_label.pack(pady=10)

try:
    img = Image.open("password_image.png")
    img = img.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack(pady=10)
except FileNotFoundError:
    messagebox.showerror("Error", "Image file not found!")

add_button = tk.Button(root, text="Add Password", command=add_password)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Password", command=remove_password)
remove_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Password", command=edit_password)
edit_button.pack(pady=5)

view_button = tk.Button(root, text="View Passwords", command=view_passwords)
view_button.pack(pady=5)

root.mainloop()