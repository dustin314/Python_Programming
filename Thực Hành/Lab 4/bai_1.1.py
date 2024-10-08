import tkinter as tk 

win =tk.Tk()

doubleData = tk.DoubleVar()
print(doubleData.get()) 
doubleData.set(2.4)
print(type(doubleData))

add_doubles = 1.222222222222222222222222 + doubleData.get()
print(add_doubles)
print(type(add_doubles))