import tkinter as tk
from tkinter import messagebox

def check_answer():
    selected_option = answer_var.get()
    if selected_option == "8":
        messagebox.showinfo("Result", "Correct! Well done.")
    else:
        messagebox.showinfo("Result", "Incorrect. The correct answer is 4.")

# Create the main window
root = tk.Tk()
root.title("Interactive Maths Quiz")

# Question label
question_label = tk.Label(root, text="What is 4 + 4?", font=("Arial", 16))
question_label.pack(pady=20)

# Variable to store the selected answer
answer_var = tk.StringVar(value="")

# Multiple choice options
options = ["2", "12", "8", "17"]
for option in options:
    radio_button = tk.Radiobutton(root, text=option, variable=answer_var, value=option, font=("Arial", 14))
    radio_button.pack(anchor="w")

# Submit button
submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 14), bg="blue", fg="white")
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
