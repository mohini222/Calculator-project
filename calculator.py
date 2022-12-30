from tkinter import*

root =Tk()
root.title("Calculator")
root.geometry("500x600")
root.resizable(0,0)

display =Label(root, font=("Arial", 20), bg="white")
display.pack(side="top", fill="both", expand=True, padx=10, pady=10)


buttons = ["7", "8", "9", "+", "C","4", "5", "6", "-","1", "2", "3", "*", "**","0", ".", "/","="]


button_grid =Frame(root)
button_grid.pack(side="top", fill="both", expand=True)
for i, button in enumerate(buttons):
    Button(button_grid, text=button, font=("Arial", 20), width=5, height=2, command=lambda x=button:process(x)).grid(row=i // 5, column=i % 5)
    

# Set up the evaluation stack
stack = []

def process(x):
    global stack
    if x == "=":
        result = str(eval(" ".join(stack)))
        stack = [result]
    elif x == "C":
        stack = []
        display.config(text="")
    else:
        stack.append(x)

    display.config(text=" ".join(stack))


root.mainloop()
