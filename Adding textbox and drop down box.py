# imports
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("MY GUI")
# Adding a label
ttk.Label(window, text = "Enter the input").grid(column=0, row=0)
ttk.Label(window, text = "choose from below").grid (column=1,row=0)

#Adding a textbox
input = tk.StringVar()
inputEntered = ttk.Entry(window, width=12, textvariable = input)
inputEntered.grid(column =0, row=1)
inputEntered.focus()

#Adding drop-down box
number=tk.StringVar();
numberChosen = ttk.Combobox(window, width=12, textvariable =number)
numberChosen['values'] = (1,2,3, 5.5, 100.7)
numberChosen.grid(column = 1, row =1)
numberChosen.current(0)



def clickButton():
    action.configure(text = 'Input is ' + input.get())
       
#Adding a button
action = ttk.Button(window, text = "Send", command = clickButton)
action.grid(column=2, row=1)


#action.configure(state='disable') #Disable the button
#win.resizable(0,0)
window.mainloop()
