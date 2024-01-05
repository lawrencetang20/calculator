import tkinter as tk
from calculator import calculate

def on_button_click(value):
  current_input.set(current_input.get() + str(value))

def clear_input():
  current_input.set("")

def calculate_result():
  expression = current_input.get()
  try:
    result = calculate(expression)
    current_input.set(result)
  except Exception as e:
    current_input.set("Error")

root = tk.Tk()
root.title("Calculator")

current_input = tk.StringVar()
current_input.set("")

entry = tk.Entry(root, textvariable=current_input, font=('Times', 30, 'bold'), justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

buttons = [
  '7', '8', '9', '/',
  '4', '5', '6', '*',
  '1', '2', '3', '-',
  '0', '(', ')', '+', '^'
]

row_val = 1
col_val = 0

for button in buttons:
  if button == 'C':
    tk.Button(root, text=button, command=clear_input, width=5, height=2, font=('Times', 20, 'bold')).grid(row=row_val, column=col_val, sticky='nsew')
  elif button in ('^', '/', '*', '-', '+'):
    tk.Button(root, text=button, command=lambda b=button: on_button_click(b), width=5, height=2, font=('Times', 20, 'bold')).grid(row=row_val, column=col_val, sticky='nsew')
  elif button in ('(', ')'):
    tk.Button(root, text=button, command=lambda b=button: on_button_click(b), width=5, height=2, font=('Times', 20, 'bold')).grid(row=row_val, column=col_val, sticky='nsew')
  else:
    tk.Button(root, text=button, command=lambda b=button: on_button_click(b), width=5, height=2, font=('Times', 20, 'bold')).grid(row=row_val, column=col_val, sticky='nsew')

  col_val += 1
  if col_val > 3:
    col_val = 0
    row_val += 1

tk.Button(root, text="Enter", command=calculate_result, width=5, height=2, font=('Times', 20, 'bold')).grid(row=row_val, column=col_val, columnspan=2, sticky='nsew')
tk.Button(root, text="Clear", command=clear_input, width=5, height=2, font=('Times', 20, 'bold')).grid(row=row_val, column=col_val + 2, columnspan=2, sticky='nsew')

for i in range(5):
  root.grid_rowconfigure(i, weight=1)
  root.grid_columnconfigure(i, weight=1)

root.mainloop()
