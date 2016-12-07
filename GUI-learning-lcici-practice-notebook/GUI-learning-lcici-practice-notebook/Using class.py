
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
    

class OOP():
    def __init__(self):
       self.window = tk.Tk()
       self.window.title("MY GUI")
       self.window.iconbitmap('@/home/chang/Documents/Python text/Chipicon.xbm')
        
       self.createWidgets()  
      
       #Button definition
    def _clickButton(self):
       self.action.configure(text = 'Input is ' + self.input.get())
      
       #Spinbox callback
    def _spin(self):
       value = self.spin.get()
       print(value)
       self.scr.insert(tk.INSERT, value +'\n')
       
       #Radiobutton callback
    def radCall(self):
       self.radSel=self.radVar.get()
       if self.radSel == 0: self.checkbox.configure (text = 'Blue')
       elif self.radSel == 1: self.checkbox.configure (text = 'Gold')
       elif self.radSel == 2: self.checkbox.configure(text = 'Red')
       
    #Menubar callback
    def _quit(self):
       self.window.quit()
       self.window.destroy()
       exit()
       
    #Menubar About Info Callback function
    def _msgBox(self):
       self.mBox.showinfo('Python Message Info Box', 'My GUI created in 2016.')
       self.mBox.showwarning('Warning Box', 'Wrong Input')
       self.answer= self.mBox.askyesno('Choice Box', 'Do you want to proceed?')
       print(self.answer)
             

    #Adding tabs  
    def createWidgets(self):
       tabControl= ttk.Notebook(self.window)
       tab1= ttk.Frame(tabControl)
       tabControl.add(tab1,text='Tab 1')
       tabControl.pack(expand=1, fill ="both")

       tab2= ttk.Frame(tabControl)
       tabControl.add(tab2, text= 'Tab 2')
       tabControl.pack(expand=1, fill ="both")

       tab3=tk.Frame(tabControl, bg = 'blue')
       tabControl.add(tab3,text='Tab 3')
       tabControl.pack(expand=1, fill ="both")
      
       for orangeColor in range(2):
           self.canvas = tk.Canvas(tab3, width =160, height =80, highlightthickness =0, bg = 'orange')
           self.canvas.grid(row=orangeColor, column= orangeColor)
       
   
     #Adding label frames
       self.enterbox = ttk.LabelFrame(tab1, text = 'Enter Box')
       self.enterbox.grid(column=0, row=0, padx=8, pady=4)

    # Adding a label
       ttk.Label(self.enterbox, text = "Enter the input").grid(column=0, row=0)
       ttk.Label(self.enterbox, text = "choose from below").grid (column=1,row=0)

    #Adding a textbox
       self.input = tk.StringVar()
       self.inputEntered = ttk.Entry(self.enterbox, width=12, textvariable = self.input)
       self.inputEntered.grid(column =0, row=1)
       self.inputEntered.focus()

    #Adding drop-down box
       self.number=tk.StringVar();
       self.numberChosen = ttk.Combobox(self.enterbox, width=12, textvariable =self.number)
       self.numberChosen['values'] = (1,2,3, 5.5, 100.7)
       self.numberChosen.grid(column = 1, row =1)
       self.numberChosen.current(0)

       
#Adding a button
       self.action = ttk.Button(self.enterbox, text = "Send", command = self._clickButton)
       self.action.grid(column=2, row=1)
       
#Adding label frames
       self.checkbox = ttk.LabelFrame(tab2, text = 'Check Box')
       self.checkbox.grid(column=0, row=0, padx=8, pady=4)
       
#Adding checkbutton
       self.chVarDis = tk.IntVar()
       self.check1 = tk.Checkbutton (self.checkbox, text = "Disabled", variable = self.chVarDis, state = 'disabled')
       self.check1.select()
       self.check1.grid(column =0, row=4, sticky = tk.W)

       self.chVarUn = tk.IntVar()
       self.check2 =tk.Checkbutton(self.checkbox, text = "UnChecked", variable = self.chVarUn)
       self.check2.deselect()
       self.check2.grid(column=1, row=4, sticky = tk.W)

       self.chVarEn = tk.IntVar()
       self.check3 = tk.Checkbutton(self.checkbox, text = "Enabled", variable = self.chVarEn)
       self.check3.select()
       self.check3.grid(column=2, row=4, sticky =tk.W)
       
#Adding label frame
       self.labelsFrame = ttk.LabelFrame(tab2, text = "Labels Frame ")
       self.labelsFrame.grid(column=0, row=7, padx=8, pady=4)

       ttk.Label(self.labelsFrame, text= "Label1").grid(column=0, row=0)
       ttk.Label(self.labelsFrame, text= "Label2").grid(column=1, row=0)
       ttk.Label(self.labelsFrame, text= "Label3").grid(column=2, row=0)
       ttk.Label(self.labelsFrame, text= "Label4").grid(column=0, row=1)

       for self.child in self.labelsFrame.winfo_children():
           self.child.grid_configure(padx=5, pady=5)
           
#Adding scrolled Text 
       scrolW = 30
       scrolH = 3
       self.scr = scrolledtext. ScrolledText(self.enterbox, width= scrolW, height=scrolH, wrap = tk.WORD)
       self.scr.grid(column=0, row =3, sticky = 'WE', columnspan =3)

       createToolTip(self.scr,'This is a ScrolledText widget')     


#Adding spinbox,action atrributed in createWidgets
       self.spin = Spinbox(self.enterbox, from_=0, to=10, width=5, command=self._spin)
       self.spin.grid(column=0, row=2)

       self.spin1 = Spinbox(self.enterbox, values = (1,2,5,8,10),width=5,bd=8)
       self.spin1.grid(column=1, row=2)
    
#Add a Tooltip to the Spinbox
       createToolTip(self.spin,'This is a Spin Contorl')
       

#Radiobutton Definition
       self.colors = ["Blue", "Gold", "Red"]
    
#Adding Radiobuttons
       self.radVar = tk.IntVar()
       
       self.radVar.set(99)  #set the default value outside the range of options

       for col in range(3) :
           self.radcol = 'rad' + str(col)
           self.radcol = tk.Radiobutton (self.checkbox, text = self.colors[col], variable = self.radVar, value
                          = col, command = self.radCall)
           self.radcol.grid(column= col, row =5, sticky = tk.W)  

#Adding Menu bar     
       self.menuBar = Menu (self.window)
       self.window.config(menu = self.menuBar)
       self.fileMenu = Menu(self.menuBar,tearoff = 0)  
       self.fileMenu.add_command(label="New")
       self.fileMenu.add_separator()
       self.fileMenu.add_command(label="Exit", command=self._quit)
       self.menuBar.add_cascade(label = "File", menu=self.fileMenu)

#Display a Message Box

    
       self.helpMenu = Menu(self.menuBar,tearoff = 0)
       self.helpMenu.add_command(label = "About",command=self._msgBox)
       self.menuBar.add_cascade (label = "Help", menu=self.helpMenu)

oop = OOP()
oop.window.mainloop()
