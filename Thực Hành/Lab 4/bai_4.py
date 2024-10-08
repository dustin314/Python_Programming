import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep
from bai_33 import GLOBAL_CONST, usingGlobal


# Tooltip class
class ToolTip:
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        self.tip_window = None
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_window is None:
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 18
            self.tip_window = tk.Toplevel(self.widget)
            self.tip_window.overrideredirect(True)
            self.tip_window.geometry(f"+{x_left}+{y_top}")
            label = tk.Label(self.tip_window, text=self.tip_text, justify=tk.LEFT, background="#ffffe0",
                             relief=tk.SOLID, borderwidth=1, font=("tahoma", "8", "normal"))
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None


# OOP class to create the main application
class OOP:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        self.win.title("Chau Gia Kiet")

        # Create widgets
        self.create_widgets()

    def click_me(self):
        # Update the button text when clicked
        self.action.configure(text='Hello ' + self.name.get() + ' ' + self.number_chosen.get())
        # Insert the Spinbox value into the ScrolledText widget
        self.strData = self.spin.get()
        self.scr.insert(tk.INSERT, "Spinbox value: " + self.strData + '\n')

        # Insert the value of GLOBAL_CONST (42) into the ScrolledText widget
        self.scr.insert(tk.INSERT, str(GLOBAL_CONST) + '\n')

        # Call the usingGlobal function and display its output (GLOBAL_CONST = 777)
        usingGlobal()  # This changes GLOBAL_CONST to 777
        self.scr.insert(tk.INSERT, "777\n")

    def create_widgets(self):
        # Create Tab Control
        tabControl = ttk.Notebook(self.win)

        # Tab 1
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')

        # Tab 2
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Tab 2')

        # Pack to make visible
        tabControl.pack(expand=1, fill="both")

        # --- Layout for Tab 1 ---
        style = ttk.Style()
        style.configure("Blue.TLabelframe.Label", foreground="Blue")
        mighty1 = ttk.LabelFrame(tab1, text=' Mighty Python ', style="Blue.TLabelframe")
        mighty1.grid(column=0, row=0, padx=8, pady=4)

        # Name Label and Entry
        ttk.Label(mighty1, text="Enter a name:").grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty1, width=12, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, padx=8, sticky=tk.W)
        self.name_entered.focus()

        # Spinbox widget
        self.spin = Spinbox(mighty1, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin)
        self.spin.grid(column=0, row=2, padx=8, sticky=tk.W)
        ToolTip(self.spin, "This is a Spin control")

        # ScrolledText widget
        scrol_w = 30
        scrol_h = 3
        self.scr = scrolledtext.ScrolledText(mighty1, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr.grid(column=0, columnspan=3, row=3, padx=8, pady=4, sticky=tk.W)
        ToolTip(self.scr, "This is a ScrolledText widget")

        # Combobox label and widget
        ttk.Label(mighty1, text="Choose a number:").grid(column=1, row=0)
        self.number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty1, width=12, textvariable=self.number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        # Action Button
        self.action = ttk.Button(mighty1, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)
        ToolTip(self.action, "This is a Button control")

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
            radSel = self.radVar.get()
            if radSel == 1:
                buttons_frame.configure(style="Blue.TLabelframe")
            elif radSel == 2:
                buttons_frame.configure(style="Gold.TLabelframe")
            elif radSel == 3:
                buttons_frame.configure(style="Red.TLabelframe")

        # Create radio buttons
        self.radVar = tk.IntVar()
        rad1 = tk.Radiobutton(mighty2, text=COLOR1, variable=self.radVar, value=1, command=radCall)
        rad2 = tk.Radiobutton(mighty2, text=COLOR2, variable=self.radVar, value=2, command=radCall)
        rad3 = tk.Radiobutton(mighty2, text=COLOR3, variable=self.radVar, value=3, command=radCall)

        rad1.grid(column=0, row=1, sticky=tk.W)
        rad2.grid(column=1, row=1, sticky=tk.W)
        rad3.grid(column=2, row=1, sticky=tk.W)

        # ProgressBar
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)

        # Progress bar controls
        buttons_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

        ttk.Button(buttons_frame, text="Run Progressbar", command=self.run_progressbar).grid(column=0, row=0, sticky='W')
        ttk.Button(buttons_frame, text="Start Progressbar", command=self.start_progressbar).grid(column=0, row=1, sticky='W')
        ttk.Button(buttons_frame, text="Stop immediately", command=self.stop_progressbar).grid(column=0, row=2, sticky='W')
        ttk.Button(buttons_frame, text="Stop after second", command=lambda: self.progressbar_stop_after(1000)).grid(column=0, row=3, sticky='W')

        # Menu Bar
        self.create_menu_bar()

    # Spinbox handler
    def _spin(self):
        value = self.spin.get()
        self.scr.insert(tk.INSERT, value + '\n')  # Insert Spinbox value into ScrolledText

    # Progressbar functions
    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)

    # Menu bar creation
    def create_menu_bar(self):
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.win.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._msgBox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    # Message box for help menu
    def _msgBox(self):
        msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter')

# Start the GUI
oop = OOP()
oop.win.mainloop()
