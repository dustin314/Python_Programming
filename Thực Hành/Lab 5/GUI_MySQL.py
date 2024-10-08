<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from os import path, makedirs
from tkinter import messagebox as mBox

# Module level GLOBALS
fDir = path.dirname(__file__)
netDir = fDir + '\\Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)

# ToolTip Class Definition
class ToolTip:
    def __init__(self, widget, text="Tooltip text"):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip_window, text=self.text, background="yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

class OOP:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        self.win.title("Chau Gia Kiet")
        self.win.resizable(0, 0)

        # Create widgets
        self.createWidgets()

    def createWidgets(self):
        # Tab Control
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='MySQL')
        tabControl.pack(expand=1, fill="both")

        # Database Frame
        self.mySQL = ttk.LabelFrame(tab1, text=' Python Database ')
        self.mySQL.grid(column=0, row=0, padx=8, pady=4)

        # Book Title Entry for Insert Quote
        ttk.Label(self.mySQL, text="Book Title:").grid(column=0, row=0, sticky='W')
        self.bookTitle_insert = ttk.Entry(self.mySQL, width=34)
        self.bookTitle_insert.grid(column=0, row=1, sticky='W')

        # Page Entry for Insert Quote
        ttk.Label(self.mySQL, text="Page:").grid(column=1, row=0, sticky='W')
        self.pageNumber_insert = ttk.Entry(self.mySQL, width=6)
        self.pageNumber_insert.grid(column=1, row=1, sticky='W')

        # Action Buttons
        self.action = ttk.Button(self.mySQL, text="Insert Quote", command=self.insertQuote)
        self.action.grid(column=2, row=1)

        # Book Title Entry for Get Quotes (without label)
        self.bookTitle_get = ttk.Entry(self.mySQL, width=34)
        self.bookTitle_get.grid(column=0, row=3, sticky='W')

        # Page Entry for Get Quotes (without label)
        self.pageNumber_get = ttk.Entry(self.mySQL, width=6)
        self.pageNumber_get.grid(column=1, row=3, sticky='W')

        # Button for Get Quotes
        self.action1 = ttk.Button(self.mySQL, text="Get Quotes", command=self.getQuote)
        self.action1.grid(column=2, row=3)

        # Book Title Entry for Modify Quote (without label)
        self.bookTitle_modify = ttk.Entry(self.mySQL, width=34)
        self.bookTitle_modify.grid(column=0, row=5, sticky='W')

        # Page Entry for Modify Quote (without label)
        self.pageNumber_modify = ttk.Entry(self.mySQL, width=6)
        self.pageNumber_modify.grid(column=1, row=5, sticky='W')

        # Button for Modify Quote
        self.action2 = ttk.Button(self.mySQL, text="Modify Quote", command=self.modifyQuote)
        self.action2.grid(column=2, row=5)

        # Tooltips
        ToolTip(self.bookTitle_insert, "Enter the book title for inserting a quote.")
        ToolTip(self.pageNumber_insert, "Enter the page number for inserting a quote.")
        ToolTip(self.bookTitle_get, "Enter the book title for retrieving quotes.")
        ToolTip(self.pageNumber_get, "Enter the page number for retrieving quotes.")
        ToolTip(self.bookTitle_modify, "Enter the book title for modifying a quote.")
        ToolTip(self.pageNumber_modify, "Enter the page number for modifying a quote.")
        ToolTip(self.action, "Click to insert a quote.")
        ToolTip(self.action1, "Click to get quotes.")
        ToolTip(self.action2, "Click to modify a quote.")

        # Quote Display Frame
        quoteFrame = ttk.LabelFrame(tab1, text=' Book Quotation ')
        quoteFrame.grid(column=0, row=1, padx=8, pady=4, columnspan=3)
        self.quote = scrolledtext.ScrolledText(quoteFrame, width=40, height=6, wrap=tk.WORD)
        self.quote.grid(column=0, row=0, sticky='WE', columnspan=3)

    def insertQuote(self):
        title = self.bookTitle_insert.get()
        page = self.pageNumber_insert.get()
        print("Inserting Quote:", title, page)

    def getQuote(self):
        title = self.bookTitle_get.get()
        page = self.pageNumber_get.get()
        print("Getting Quotes for:", title, page)
        self.quote.insert(tk.INSERT, f"Sample quote for {title} on page {page}\n")

    def modifyQuote(self):
        title = self.bookTitle_modify.get()
        page = self.pageNumber_modify.get()
        print("Modifying Quote for:", title, page)

# Start GUI
oop = OOP()
=======
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from os import path, makedirs
from tkinter import messagebox as mBox

# Module level GLOBALS
fDir = path.dirname(__file__)
netDir = fDir + '\\Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)

# ToolTip Class Definition
class ToolTip:
    def __init__(self, widget, text="Tooltip text"):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip_window, text=self.text, background="yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

class OOP:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        self.win.title("Chau Gia Kiet")
        self.win.resizable(0, 0)

        # Create widgets
        self.createWidgets()

    def createWidgets(self):
        # Tab Control
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='MySQL')
        tabControl.pack(expand=1, fill="both")

        # Database Frame
        self.mySQL = ttk.LabelFrame(tab1, text=' Python Database ')
        self.mySQL.grid(column=0, row=0, padx=8, pady=4)

        # Book Title Entry for Insert Quote
        ttk.Label(self.mySQL, text="Book Title:").grid(column=0, row=0, sticky='W')
        self.bookTitle_insert = ttk.Entry(self.mySQL, width=34)
        self.bookTitle_insert.grid(column=0, row=1, sticky='W')

        # Page Entry for Insert Quote
        ttk.Label(self.mySQL, text="Page:").grid(column=1, row=0, sticky='W')
        self.pageNumber_insert = ttk.Entry(self.mySQL, width=6)
        self.pageNumber_insert.grid(column=1, row=1, sticky='W')

        # Action Buttons
        self.action = ttk.Button(self.mySQL, text="Insert Quote", command=self.insertQuote)
        self.action.grid(column=2, row=1)

        # Book Title Entry for Get Quotes (without label)
        self.bookTitle_get = ttk.Entry(self.mySQL, width=34)
        self.bookTitle_get.grid(column=0, row=3, sticky='W')

        # Page Entry for Get Quotes (without label)
        self.pageNumber_get = ttk.Entry(self.mySQL, width=6)
        self.pageNumber_get.grid(column=1, row=3, sticky='W')

        # Button for Get Quotes
        self.action1 = ttk.Button(self.mySQL, text="Get Quotes", command=self.getQuote)
        self.action1.grid(column=2, row=3)

        # Book Title Entry for Modify Quote (without label)
        self.bookTitle_modify = ttk.Entry(self.mySQL, width=34)
        self.bookTitle_modify.grid(column=0, row=5, sticky='W')

        # Page Entry for Modify Quote (without label)
        self.pageNumber_modify = ttk.Entry(self.mySQL, width=6)
        self.pageNumber_modify.grid(column=1, row=5, sticky='W')

        # Button for Modify Quote
        self.action2 = ttk.Button(self.mySQL, text="Modify Quote", command=self.modifyQuote)
        self.action2.grid(column=2, row=5)

        # Tooltips
        ToolTip(self.bookTitle_insert, "Enter the book title for inserting a quote.")
        ToolTip(self.pageNumber_insert, "Enter the page number for inserting a quote.")
        ToolTip(self.bookTitle_get, "Enter the book title for retrieving quotes.")
        ToolTip(self.pageNumber_get, "Enter the page number for retrieving quotes.")
        ToolTip(self.bookTitle_modify, "Enter the book title for modifying a quote.")
        ToolTip(self.pageNumber_modify, "Enter the page number for modifying a quote.")
        ToolTip(self.action, "Click to insert a quote.")
        ToolTip(self.action1, "Click to get quotes.")
        ToolTip(self.action2, "Click to modify a quote.")

        # Quote Display Frame
        quoteFrame = ttk.LabelFrame(tab1, text=' Book Quotation ')
        quoteFrame.grid(column=0, row=1, padx=8, pady=4, columnspan=3)
        self.quote = scrolledtext.ScrolledText(quoteFrame, width=40, height=6, wrap=tk.WORD)
        self.quote.grid(column=0, row=0, sticky='WE', columnspan=3)

    def insertQuote(self):
        title = self.bookTitle_insert.get()
        page = self.pageNumber_insert.get()
        print("Inserting Quote:", title, page)

    def getQuote(self):
        title = self.bookTitle_get.get()
        page = self.pageNumber_get.get()
        print("Getting Quotes for:", title, page)
        self.quote.insert(tk.INSERT, f"Sample quote for {title} on page {page}\n")

    def modifyQuote(self):
        title = self.bookTitle_modify.get()
        page = self.pageNumber_modify.get()
        print("Modifying Quote for:", title, page)

# Start GUI
oop = OOP()
>>>>>>> a6dc84ab8684f0becaf28d314ed0711d4739a8d2
oop.win.mainloop()