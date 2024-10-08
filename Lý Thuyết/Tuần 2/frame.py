import tkinter as tk
from tkinter import ttk

def cong():
    result = a.get() + b.get()
    ketqua_label.config(text=f"Kết quả: {result}")

def tru():
    result = a.get() - b.get()
    ketqua_label.config(text=f"Kết quả: {result}")

def nhan():
    result = a.get() * b.get()
    ketqua_label.config(text=f"Kết quả: {result}")

def chia():
    if b.get() != 0:
        result = a.get() / b.get()
        ketqua_label.config(text=f"Kết quả: {result}")
    else:
        ketqua_label.config(text="Lỗi: Không thể chia cho 0")


win = tk.Tk()
win.title("Tính Toán")

# Tạo frame nhập số
nhapso_frame = ttk.LabelFrame(win, text="Nhập số")
nhapso_frame.grid(column=0, row=0, padx=10, pady=10)

# Tạo 2 label và entry để nhập số a và b
ttk.Label(nhapso_frame, text="Nhập số a:").grid(column=0, row=0, sticky=tk.W)
ttk.Label(nhapso_frame, text="Nhập số b:").grid(column=0, row=1, sticky=tk.W)

a = tk.IntVar()
a_entry = ttk.Entry(nhapso_frame, width=12, textvariable=a)
a_entry.grid(column=1, row=0)
a_entry.focus()

b = tk.IntVar()
b_entry = ttk.Entry(nhapso_frame, width=12, textvariable=b)
b_entry.grid(column=1, row=1)

# Tạo frame tính toán
tinhtoan_frame = ttk.LabelFrame(win, text="Tính toán")
tinhtoan_frame.grid(column=1, row=0, padx=10, pady=10)

# Tạo các button để thực hiện phép tính
ttk.Button(tinhtoan_frame, text="+", command=cong).grid(column=0, row=0, padx=5, pady=5)
ttk.Button(tinhtoan_frame, text="-", command=tru).grid(column=1, row=0, padx=5, pady=5)
ttk.Button(tinhtoan_frame, text="*", command=nhan).grid(column=0, row=1, padx=5, pady=5)
ttk.Button(tinhtoan_frame, text="/", command=chia).grid(column=1, row=1, padx=5, pady=5)

# Thêm Label để hiện kết quả
ketqua_label = ttk.Label(win, text="Kết quả: ")
ketqua_label.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

win.mainloop()