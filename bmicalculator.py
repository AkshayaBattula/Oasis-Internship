import tkinter as tk
from tkinter import messagebox

# Function to determine BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "blue", (
            "Your BMI is below the standard range. With proper nutrition and care, "
            "you can build strength and energy over time."
        )
    elif bmi < 25:
        return "Normal", "green", (
            "Excellent! Your BMI falls within a healthy range. "
            "Maintain your routine and continue prioritizing your well-being."
        )
    elif bmi < 30:
        return "Overweight", "orange", (
            "You're close to the healthy range. Consistent habits and balance "
            "can lead to positive outcomes."
        )
    else:
        return "Obese", "red", (
            "Your health journey is important and personal. "
            "Small, steady improvements can make a meaningful difference."
        )

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showwarning("Invalid Input", "Weight and height must be greater than zero.")
            return

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        category, color, message = get_bmi_category(bmi)

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}\n\n{message}",
            fg=color
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Function to clear all fields
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Male")
    result_label.config(text="", fg="black")
    weight_entry.focus()

# Main window
window = tk.Tk()
window.title("Enhanced BMI Calculator")
window.geometry("420x360")
window.configure(bg="#f5f5dc")

# Weight
tk.Label(window, text="Weight (kg):", bg="#f5f5dc", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
weight_entry = tk.Entry(window, font=("Arial", 11))
weight_entry.grid(row=0, column=1)

# Height
tk.Label(window, text="Height (cm):", bg="#f5f5dc", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
height_entry = tk.Entry(window, font=("Arial", 11))
height_entry.grid(row=1, column=1)

# Age (optional)
tk.Label(window, text="Age:", bg="#f5f5dc", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
age_entry = tk.Entry(window, font=("Arial", 11))
age_entry.grid(row=2, column=1)

# Gender selection
tk.Label(window, text="Gender:", bg="#f5f5dc", font=("Arial", 11)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar(value="Male")

gender_frame = tk.Frame(window, bg="#f5f5dc")
gender_frame.grid(row=3, column=1, sticky="w")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#f5f5dc").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#f5f5dc").pack(side="left")

# Buttons
button_frame = tk.Frame(window, bg="#f5f5dc")
button_frame.grid(row=4, column=0, columnspan=2, pady=15)

tk.Button(button_frame, text="Calculate", bg="darkgreen", fg="white", font=("Arial", 11),
          command=calculate_bmi).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Clear", bg="darkred", fg="white", font=("Arial", 11),
          command=clear_fields).grid(row=0, column=1, padx=10)

# Result
result_label = tk.Label(
    window,
    text="",
    bg="#f5f5dc",
    font=("Arial", 12),
    wraplength=360,
    justify="center"
)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
