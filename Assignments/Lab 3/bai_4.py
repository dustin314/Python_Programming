import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

# Create main window
win = tk.Tk()
win.title("Chau Gia Kiet")

# Create a tab control (notebook)
tabControl = ttk.Notebook(win)

# Create Tab 1
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill="both")

# Create Tab 2
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

# --- Layout for Tab 1 ---
style = ttk.Style()
style.configure("Blue.TLabelframe.Label", foreground="Blue")
mighty1 = ttk.LabelFrame(tab1, text=' Mighty Python ', style="Blue.TLabelframe")  
mighty1.grid(column=0, row=0, padx=8, pady=4)

# Inside the mighty LabelFrame (Tab 1), add widgets
ttk.Label(mighty1, text="Enter a name:").grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)

name = tk.StringVar()
name_entered = ttk.Entry(mighty1, width=12, textvariable=name)
name_entered.grid(column=0, row=1, padx=20, sticky=tk.W)

ttk.Label(mighty1, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty1, width=12, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Action Button
action = ttk.Button(mighty1, text="Click Me!", command=lambda: action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get()))
action.grid(column=2, row=1)

# ScrolledText widget for Tab 1
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty1, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, row=3)

# --- Layout for Tab 2 ---
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ', style="Blue.TLabelframe")
mighty2.grid(column=0, row=0, padx=8, pady=4)

# Checkbuttons in Tab 2
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=0, sticky=tk.W)

# Radiobuttons for color in Tab 2
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        buttons_frame.configure(style="Blue.TLabelframe")
    elif radSel == 2:
        buttons_frame.configure(style="Gold.TLabelframe")
    elif radSel == 3:
        buttons_frame.configure(style="Red.TLabelframe")

# Create radio buttons
radVar = tk.IntVar()
rad1 = tk.Radiobutton(mighty2, text=COLOR1, variable=radVar, value=1, command=radCall)
rad2 = tk.Radiobutton(mighty2, text=COLOR2, variable=radVar, value=2, command=radCall)
rad3 = tk.Radiobutton(mighty2, text=COLOR3, variable=radVar, value=3, command=radCall)

rad1.grid(column=0, row=1, sticky=tk.W)
rad2.grid(column=1, row=1, sticky=tk.W)
rad3.grid(column=2, row=1, sticky=tk.W)

# Additional frame in Tab 2 for labels
style.configure("Gold.TLabelframe.Label", foreground="Gold")
style.configure("Red.TLabelframe.Label", foreground="Red")

buttons_frame = ttk.LabelFrame(mighty2, text='Labels in a Frame', style="Blue.TLabelframe")
buttons_frame.grid(column=0, row=2, columnspan=3, pady=10)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

# Add a menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()

file_menu.add_command(label="Exit", command=win.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

def _msgBox():
    msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2019.')

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command = _msgBox)
menu_bar.add_cascade(label="Help", menu=help_menu)

win.iconbitmap('favicon.ico')

# Set focus to the name entry field
name_entered.focus()

# Start the GUI event loop
win.mainloop()
