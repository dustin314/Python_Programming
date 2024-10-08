import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep

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

tab3 = ttk.Frame(tabControl)  
tabControl.add(tab3, text='Tab 3')

tabControl.pack(expand=1, fill="both")
tab3_frame = tk.Frame(tab3, bg='blue')  
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80,  highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)


# --- Layout for Tab 1 ---
style = ttk.Style()
style.configure("Blue.TLabelframe.Label", foreground="Blue")
mighty1 = ttk.LabelFrame(tab1, text=' Mighty Python ', style="Blue.TLabelframe")  
mighty1.grid(column=0, row=0, padx=8, pady=4)

# Inside the mighty LabelFrame (Tab 1), add widgets
ttk.Label(mighty1, text="Enter a name:").grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)
class ToolTip(object):
    def __init__(self, widget, tip_text=None):  # Fix here (double underscores)
        self.widget = widget
        self.tip_text = tip_text
        self.tip_window = None  # Initialize tip_window to None
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):  
        self.show_tooltip()

    def mouse_leave(self, _event):  
        self.hide_tooltip()

    def show_tooltip(self):  
        if self.tip_window is None:  # Add this condition to ensure only one tooltip window is created
            x_left = self.widget.winfo_rootx()  
            y_top = self.widget.winfo_rooty() - 18
            self.tip_window = tk.Toplevel(self.widget) 
            self.tip_window.overrideredirect(True)
            self.tip_window.geometry("+%d+%d" % (x_left, y_top))  
            label = tk.Label(self.tip_window, text=self.tip_text,  justify=tk.LEFT, background="#ffffe0", relief=tk.SOLID,  borderwidth=1, font=("tahoma", "8", "normal"))  
            label.pack(ipadx=1)

    def hide_tooltip(self):  
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None  # Reset tip_window to None after hiding

def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin = Spinbox(mighty1, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin)
spin.grid(column=0, row=2, padx=8, sticky=tk.W)  # Align spinbox to the left
ToolTip(spin, 'This is a Spin control')

name = tk.StringVar()
name_entered = ttk.Entry(mighty1, width=12, textvariable=name)
name_entered.grid(column=0, row=1, padx=8, sticky=tk.W)  # Align entry field to the left

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
scr.grid(column=0, columnspan=3, row=3, padx=8, pady=4, sticky=tk.W)  # Align scrolledtext to the left
ToolTip(scr, 'This is a ScrolledText widget')
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

# ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
# ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
# ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

colors = [COLOR1, COLOR2, COLOR3]
for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col],  variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=1, sticky=tk.W)
progress_bar = ttk.Progressbar(tab2, orient='horizontal',  length=286, mode='determinate')  
progress_bar.grid(column=0, row=3, pady=2)

def run_progressbar():
    progress_bar["maximum"] =100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i  
        progress_bar.update()
        progress_bar["value"] = 0

def start_progressbar():  progress_bar.start()

def stop_progressbar():  progress_bar.stop()

def progressbar_stop_after(wait_ms=1000):  win.after(wait_ms, progress_bar.stop)

buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')  
buttons_frame.grid(column=0, row=7)

buttons_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')  
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

ttk.Button(buttons_frame, text=" Run Progressbar ",  command=run_progressbar).grid(column=0, row=0, sticky='W')  
ttk.Button(buttons_frame, text=" Start Progressbar ",  command=start_progressbar).grid(column=0, row=1, sticky='W')  
ttk.Button(buttons_frame, text=" Stop immediately ",  command=stop_progressbar).grid(column=0, row=2, sticky='W')  
ttk.Button(buttons_frame, text=" Stop after second ",
command=progressbar_stop_after).grid(column=0, row=3, sticky='W')

for child in buttons_frame.winfo_children():
	child.grid_configure(padx=2, pady=2)
 
for child in mighty2.winfo_children():  
    child.grid_configure(padx=8, pady=2)
    

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
