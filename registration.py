import tkinter as tk
from tkinter import messagebox

# Function to handle registration
def register():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    
    if not name or not email or not password or gender not in ['Male', 'Female']:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Registration Successful!\nName: {name}\nEmail: {email}\nGender: {gender}")

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Heading Label
tk.Label(root, text="User Registration", font=("Arial", 16, "bold"), fg="#4A90E2", bg="#f0f0f0").pack(pady=10)

# Labels and Entry Widgets
tk.Label(root, text="Name", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_name = tk.Entry(root, font=("Arial", 12), width=30)
entry_name.pack()

tk.Label(root, text="Email", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_email = tk.Entry(root, font=("Arial", 12), width=30)
entry_email.pack()

tk.Label(root, text="Password", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_password = tk.Entry(root, font=("Arial", 12), width=30, show="*")
entry_password.pack()

# Gender Selection
gender_var = tk.StringVar(value="None")
tk.Label(root, text="Gender", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
gender_frame = tk.Frame(root, bg="#f0f0f0")
gender_frame.pack()
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=10)

# Register Button
tk.Button(root, text="Register", font=("Arial", 12, "bold"), bg="#4A90E2", fg="white", width=15, command=register).pack(pady=20)

# Run the application
root.mainloop()