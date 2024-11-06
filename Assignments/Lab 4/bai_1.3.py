import tkinter as tk 

win =tk.Tk()

strData = tk.StringVar()

strData.set('Hello StringVar')

varData = strData.get()

print(varData)

print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())