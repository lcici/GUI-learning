
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x =self.y =0
        
    def showtip(self,text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self. widget.winfo_rootx() +27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel (self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x,y))
        
        label = tk.Label(tw, text = self. text, justify = tk.LEFT,
                         background ="#ffffe0", relief = tk.SOLID, borderwidth =1,
                         font = ("tahoma", "8", "normal"))
        label.pack(ipadx=1)
        
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            
def createToolTip (widget, text):
    toolTip = ToolTip (widget)
    def enter(event) :
        toolTip.showtip(text)
    def leave (event):
        toolTip.hidetip()
    widget.bind('<Enter>',enter)
    widget.bind('<Leave>',leave)
    

window = tk.Tk()
window.title("MY GUI")
window.iconbitmap('@/home/chang/Documents/Python text/Chipicon.xbm')

#Adding tabs
tabControl = ttk.Notebook(window)
tab1= ttk.Frame(tabControl)
tabControl.add(tab1,text='Tab 1')
tabControl.pack(expand=1, fill ="both")

tab2= ttk.Frame(tabControl)
tabControl.add(tab2, text= 'Tab 2')

#Adding label frames
enterbox = ttk.LabelFrame(tab1, text = 'Enter Box')
enterbox.grid(column=0, row=0, padx=8, pady=4)

# Adding a label
ttk.Label(enterbox, text = "Enter the input").grid(column=0, row=0)
ttk.Label(enterbox, text = "choose from below").grid (column=1,row=0)

#Adding a textbox
input = tk.StringVar()
inputEntered = ttk.Entry(enterbox, width=12, textvariable = input)
inputEntered.grid(column =0, row=1)
inputEntered.focus()

#Adding drop-down box
number=tk.StringVar();
numberChosen = ttk.Combobox(enterbox, width=12, textvariable =number)
numberChosen['values'] = (1,2,3, 5.5, 100.7)
numberChosen.grid(column = 1, row =1)
numberChosen.current(0)


#Button definition
def clickButton():
    action.configure(text = 'Input is ' + input.get())
       
#Adding a button
action = ttk.Button(enterbox, text = "Send", command = clickButton)
action.grid(column=2, row=1)


#Adding spinbox
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value +'\n')
spin = Spinbox(enterbox, from_=0, to=10, width=5, command=_spin)
spin.grid(column=0, row=2)

spin1 = Spinbox(enterbox, values = (1,2,5,8,10),width=5,bd=8)
spin1.grid(column=1, row=2)

#Add a Tooltip to the Spinbox
createToolTip(spin,'This is a Spin Contorl')

#Adding scrolled Text 
scrolW = 30
scrolH = 3
scr = scrolledtext. ScrolledText(enterbox, width= scrolW, height=scrolH, wrap = tk.WORD)
scr.grid(column=0, sticky = 'WE', columnspan =3)

createToolTip(scr,'This is a ScrolledText widget')

#Adding label frames
checkbox = ttk.LabelFrame(tab2, text = 'Check Box')
checkbox.grid(column=0, row=0, padx=8, pady=4)

#Adding checkbutton

chVarDis = tk.IntVar()
check1 = tk.Checkbutton (checkbox, text = "Disabled", variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column =0, row=4, sticky = tk.W)

chVarUn = tk.IntVar()
check2 =tk.Checkbutton(checkbox, text = "UnChecked", variable = chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky = tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(checkbox, text = "Enabled", variable = chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky =tk.W)

#Radiobutton Definition
colors = ["Blue", "Gold", "Red"]


##Radiobutton 
def radCall():
    radSel=radVar.get()
    if radSel == 0: checkbox.configure (text = 'Blue')
    elif radSel == 1: checkbox.configure (text = 'Gold')
    elif radSel == 2: checkbox.configure(text = 'Red')
    
#Adding Radiobuttons
radVar = tk.IntVar()

radVar.set(99)  #set the default value outside the range of options

for col in range(3) :
    radcol = 'rad' + str(col)
    radcol = tk.Radiobutton (checkbox, text = colors[col], variable = radVar, value
                          = col, command = radCall)
    radcol.grid(column= col, row =5, sticky = tk.W)
    
#Adding label frame
labelsFrame = ttk.LabelFrame(tab2, text = "Labels Frame ")
labelsFrame.grid(column=0, row=7, padx=8, pady=4)

ttk.Label(labelsFrame, text= "Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text= "Label2").grid(column=1, row=0)
ttk.Label(labelsFrame, text= "Label3").grid(column=2, row=0)
ttk.Label(labelsFrame, text= "Label4").grid(column=0, row=1)

for child in labelsFrame.winfo_children():
  child.grid_configure(padx=5, pady=5)

#Adding Menu bar
def _quit():
    window.quit()
    window.destroy()
    exit()
    
menuBar = Menu (window)
window.config(menu = menuBar)

fileMenu = Menu(menuBar,tearoff = 0)  
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label = "File", menu=fileMenu)

#Display a Message Box
#Callback function
def _msgBox():
#   mBox.showinfo('Python Message Info Box', 'My GUI created in 2016.')
#   mBox.showwarning('Warning Box', 'Wrong Input')
#   mBox.showerror('Error Box', 'Error Input')
    answer= mBox.askyesno('Choice Box', 'Do you want to proceed?')
    print(answer)
    
helpMenu = Menu(menuBar,tearoff = 0)
helpMenu.add_command(label = "About",command=_msgBox)
menuBar.add_cascade (label = "Help", menu=helpMenu)


window.mainloop()
