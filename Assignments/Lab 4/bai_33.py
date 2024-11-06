import tkinter as tk
win = tk.Tk()

GLOBAL_CONST = 42 
print(GLOBAL_CONST)

def usingGlobal():
    GLOBAL_CONST = 777 
    print(GLOBAL_CONST)

usingGlobal()

print('GLOBAL_CONST:', GLOBAL_CONST)