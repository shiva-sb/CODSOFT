import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    label_result.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets for numbers and operation choice
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0)

operation_var = tk.StringVar(root)
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")  # Default operation choice
operation_menu = tk.OptionMenu(root, operation_var, *operation_choices)
operation_menu.grid(row=0, column=1)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=2)

# Create button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1)

# Create label to display result
label_result = tk.Label(root, text="")
label_result.grid(row=2, columnspan=3)

root.mainloop()
