import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

# Create main window
win = tk.Tk()
win.title("Chau Gia Kiet")

# Define the click event for the button
def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())

# Create a container frame for the border effect
border_frame = tk.Frame(win, bd=0, relief="solid")
border_frame.grid(column=0, row=0, padx=8, pady=4, columnspan=3, sticky=tk.W)

style = ttk.Style()
style.configure("Blue.TLabelframe.Label", foreground="Blue")
mighty = ttk.LabelFrame(border_frame, text=' Mighty Python ', style="Blue.TLabelframe")  
mighty.grid(column=0, row=0)

# Inside the mighty LabelFrame, add widgets
ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)

# Adjust the name_entered widget with padx to move it slightly to the right
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, padx=20, sticky=tk.W)  # Adjusted padx to move it right

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Action Button
action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

# Checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

# Radiobuttons for color
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(bg=COLOR1)  # Blue border surrounding the entire window
    elif radSel == 2:
        win.configure(bg=COLOR2)  # Gold border surrounding the entire window
    elif radSel == 3:
        win.configure(bg=COLOR3)  # Red border surrounding the entire window

radVar = tk.IntVar()
rad1 = tk.Radiobutton(mighty, text=COLOR1, variable=radVar, value=1, command=radCall)
rad2 = tk.Radiobutton(mighty, text=COLOR2, variable=radVar, value=2, command=radCall)
rad3 = tk.Radiobutton(mighty, text=COLOR3, variable=radVar, value=3, command=radCall)

rad1.grid(column=0, row=4, sticky=tk.W)  
rad2.grid(column=1, row=4, sticky=tk.W)  
rad3.grid(column=2, row=4, sticky=tk.W)

# ScrolledText widget
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, row=3)

# Create an additional LabelFrame with labels, without a border (relief="flat")
style = ttk.Style()
style.configure("Blue.TLabelframe.Label", foreground="Blue")
buttons_frame = ttk.LabelFrame(border_frame, text='Labels in a Frame', style="Blue.TLabelframe", relief="flat")
buttons_frame.grid(column=0, row=5, sticky=tk.W, padx=0)  # Align to the left (W), no padding

# Adding labels inside the buttons_frame
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu_bar.add_cascade(label="File", menu=file_menu)


# Set focus to the name entry field
name_entered.focus()

# Start the GUI event loop
win.mainloop()
