import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Chau Gia Kiet")

def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())

border_frame = tk.Frame(win, bd=1, relief="solid")
border_frame.grid(column=0, row=0, padx=8, pady=4, columnspan=3)

mighty = ttk.LabelFrame(border_frame, text=' Mighty Python ')  
mighty.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0)
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

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

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(bg=COLOR1)  
    elif radSel == 2:
        win.configure(bg=COLOR2)  
    elif radSel == 3:
        win.configure(bg=COLOR3)  

radVar = tk.IntVar()
rad1 = tk.Radiobutton(mighty, text=COLOR1, variable=radVar, value=1, command=radCall)
rad2 = tk.Radiobutton(mighty, text=COLOR2, variable=radVar, value=2, command=radCall)
rad3 = tk.Radiobutton(mighty, text=COLOR3, variable=radVar, value=3, command=radCall)

rad1.grid(column=0, row=4, sticky=tk.W)  
rad2.grid(column=1, row=4, sticky=tk.W)  
rad3.grid(column=2, row=4, sticky=tk.W)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, row=3)

style = ttk.Style()
style.configure("Blue.TLabelframe.Label", foreground="Blue")
buttons_frame = ttk.LabelFrame(border_frame, text='Labels in a Frame', style="Blue.TLabelframe", relief="flat")
buttons_frame.grid(column=0, row=5, columnspan=3, pady=10)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

name_entered.focus()


win.mainloop()