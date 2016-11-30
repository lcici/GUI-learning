# imports
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("MY GUI")
# Adding a label
#aLabel = ttk.Label(window, text = "Label A").grid(column=0, row=0)
aLabel = ttk.Label(window, text = "Label A")
aLabel.grid(column=0, row=0)          #assigning the label to a variable
#Button clickable
def clickButton():
    action.configure(text="** Click Done **")
    aLabel.configure(foreground = 'red')
    
#Adding a Button
action = ttk.Button(window, text="Click me", command=clickButton)
action.grid(column=1, row=0)

#win.resizable(0,0)
window.mainloop()
