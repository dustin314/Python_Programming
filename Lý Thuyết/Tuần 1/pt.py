import tkinter as tk
from tkinter import ttk 

def click_me():
    result = a.get() + b.get()  # Cộng hai kết quả 
    action.configure(text=f"Result: {result}")  # Trả về kết quả

if __name__ == '__main__':
    win = tk.Tk()
    win.title("Python GUI")

    # Labels
    ttk.Label(win, text="Nhập số a:").grid(column=0, row=0)
    ttk.Label(win, text="Nhập số b:").grid(column=0, row=1)

    a = tk.IntVar()
    a_entry = ttk.Entry(win, width=12, textvariable=a)
    a_entry.grid(column=1, row=0)

    b = tk.IntVar()
    b_entry = ttk.Entry(win, width=12, textvariable=b)
    b_entry.grid(column=1, row=1)

    # Button
    action = ttk.Button(win, text="Click Me!", command=click_me)
    action.grid(column=1, row=2)

    win.mainloop()