
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


#Button definition
def clickButton():
    action.configure(text = 'Input is ' + input.get())
       
#Adding a button
action = ttk.Button(window, text = "Send", command = clickButton)
action.grid(column=2, row=1)

#Adding checkbutton

chVarDis = tk.IntVar()
check1 = tk.Checkbutton (window, text = "Disabled", variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column =0, row=4, sticky = tk.W)

chVarUn = tk.IntVar()
check2 =tk.Checkbutton(window, text = "UnChecked", variable = chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky = tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(window, text = "Enabled", variable = chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky =tk.W)

#Radiobutton Definition
COLOR1 = "Red"
COLOR2 = "Gold"
COLOR3 = "Blue"

##Radiobutton 
def radCall():
    radSel=radVar.get()
    if radSel == 1: window.configure (background = COLOR1)
    elif radSel == 2: window.configure (background = COLOR2)
    elif radSel == 3: window.configure(background = COLOR3)
    
  #Adding Radiobuttons
radVar = tk.IntVar()
rad1 = tk. Radiobutton (window, text = COLOR1, variable = radVar, value=1, command = radCall)
rad1.grid(column = 0, row =5, sticky = tk.W)

rad2= tk.Radiobutton(window, text= COLOR2, variable = radVar, value=2, command= radCall)
rad2.grid(column=1, row=5, sticky=tk.W)

rad3 = tk.Radiobutton (window, text= COLOR3, variable = radVar, value=3, command = radCall)
rad3.grid(column=2, row=5, sticky=tk.W)


#action.configure(state='disable') #Disable the button
#win.resizable(0,0)
window.mainloop()
