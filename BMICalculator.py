import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        label_result.config(text=f"BMI: {bmi} ({category})", fg="blue")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for height and weight.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.resizable(False, False)


tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

tk.Label(root, text="Enter height (cm):").pack()
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack()


root.mainloop()
