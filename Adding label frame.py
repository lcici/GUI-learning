# imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
colors = ["Blue", "Gold", "Red"]


##Radiobutton 
def radCall():
    radSel=radVar.get()
    if radSel == 0: window.configure (background = colors[0])
    elif radSel == 1: window.configure (background = colors[1])
    elif radSel == 2: window.configure(background = colors[2])
    
  #Adding Radiobuttons
radVar = tk.IntVar()

radVar.set(99)  #set the default value outside the range of options

for col in range(3) :
    radcol = 'rad' + str(col)
    radcol = tk.Radiobutton (window, text = colors[col], variable = radVar, value
                          = col, command = radCall)
    radcol.grid(column= col, row =5, sticky = tk.W)


#Adding scrolled Text 
scrolW = 30
scrolH = 3
scr = scrolledtext. ScrolledText(window, width= scrolW, height=scrolH, wrap = tk.WORD)
scr.grid(column=0, sticky = 'WE', columnspan =3)

#Using Label Frame function
labelsFrame = ttk.LabelFrame(window, text = "Labels Frame ")
labelsFrame.grid(column=1, row=7, padx=20, pady=10)

ttk.Label(labelsFrame, text= "Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text= "Label2").grid(column=1, row=0)
ttk.Label(labelsFrame, text= "Label3").grid(column=2, row=0)
ttk.Label(labelsFrame, text= "Label4").grid(column=0, row=1)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)



#action.configure(state='disable') #Disable the button
#win.resizable(0,0)
window.mainloop()
