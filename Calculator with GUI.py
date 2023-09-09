# pip install tk for installation of tkinter

import tkinter as tk

# Function to update the display with button clicks
def button_click(event):
    current_text = display.get("1.0",tk.END)
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            display.delete(1.0, tk.END)  # Clear the current text
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(1.0, tk.END)  # Clear the current text
            display.insert(tk.END, "Error")
    elif button_text == "C":
        display.delete(1.0, tk.END)  # Clear the current text
    else:
        display.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a text entry field (display)
display = tk.Text(root, height=2, width=16, font=("Arial", 24))
display.grid(row=0, column=0, columnspan=4)

# Create calculator buttons
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_num = 1
col_num = 0

for text in button_texts:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18))
    button.grid(row=row_num, column=col_num)
    button.bind("<Button-1>", button_click)

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Run the Tkinter main loop
root.mainloop()

# In this code:

# 1. We import the tkinter library and create a Tk object as the main window.

# 2. We define a function button_click to update the display text when calculator buttons are clicked. It handles button clicks, evaluates expressions when the "=" button is clicked, and clears the display when the "C" button is clicked.

# 3. We create a text entry field (display) using the Text widget and place it at the top of the window.

# 4. We create calculator buttons with the specified text and bind the button_click function to them. These buttons are arranged in a 4x4 grid.

# 5. Finally, we start the Tkinter main loop with root.mainloop(), which allows the GUI to interact with the user.