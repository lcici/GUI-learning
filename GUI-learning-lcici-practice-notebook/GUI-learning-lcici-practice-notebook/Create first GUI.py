

# imports
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("MY GUI")
# Adding a label
ttk.Label(window, text = "Label A").grid(column=0, row=0)

#win.resizable(0,0)
window.mainloop()
