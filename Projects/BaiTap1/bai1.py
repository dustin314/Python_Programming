# Thêm các thư viện cần thiết 
import tkinter as tk 
from tkinter import ttk 
from tkinter import Menu 
from tkinter import messagebox as msg # Hộp thoại cảnh báo 

class OOP: 
    def __init__(self):
        # Khởi tạo 
        self.win = tk.Tk()
        # Title 
        self.win.title("Python GUI")

        # Tạo menu bar
        self.create_menu_bar()
        # Tạo các Tab 
        self.create_widgets()

    def create_menu_bar(self):
        # Tạo menu bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # File menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu) # Tạo ra menu thứ nhất
        # Các mục con
        file_menu.add_command(label="New", command=self.create_new_tab)  # Tạo thêm tab mới
        file_menu.add_separator() # Gạch chân nét liền 
        file_menu.add_command(label="Exit", command=self._msgExit) # Thoát khỏi chương trình

        # Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        # Các mục con 
        help_menu.add_command(label="About")

    # Hộp thoại cảnh báo cho nút exit
    def _msgExit(self):
        response = msg.askyesnocancel("Python Message Box", 'Bạn sẽ rời khỏi chương trình \nBạn chắc chứ?')
        if response:  # Nếu bấm 'Yes'
            self.win.quit()  # Rời khỏi chương trình 

    def create_widgets(self):
        # Tạo TabControl
        self.tabControl = ttk.Notebook(self.win)

        # Tab 1 
        tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(tab1, text='Tab 1')

        # Tab 2 - To-Do List
        tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(tab2, text='Tab 2')

        self.tabControl.pack(expand=1, fill='both')

        # Tạo frame nhập số trong tab 1
        nhapso_frame = ttk.LabelFrame(tab1, text="Nhập số")
        nhapso_frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(nhapso_frame, text="Nhập số a:").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(nhapso_frame, text="Nhập số b:").grid(column=0, row=1, sticky=tk.W)

        # Các biến IntVar để lưu trữ giá trị của a và b
        self.a = tk.IntVar()
        self.b = tk.IntVar()

        # Entry nhập số a
        a_entry = ttk.Entry(nhapso_frame, width=12, textvariable=self.a)
        a_entry.grid(column=1, row=0)
        a_entry.focus()

        # Entry nhập số b
        b_entry = ttk.Entry(nhapso_frame, width=12, textvariable=self.b)
        b_entry.grid(column=1, row=1)

        # Frame cho các nút tính toán
        tinhtoan_frame = ttk.LabelFrame(tab1, text="Tính toán")
        tinhtoan_frame.grid(column=1, row=0, padx=10, pady=10)

        # Các nút tính toán
        ttk.Button(tinhtoan_frame, text="+", command=self.cong).grid(column=0, row=0, padx=5, pady=5)
        ttk.Button(tinhtoan_frame, text="-", command=self.tru).grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(tinhtoan_frame, text="*", command=self.nhan).grid(column=0, row=1, padx=5, pady=5)
        ttk.Button(tinhtoan_frame, text="/", command=self.chia).grid(column=1, row=1, padx=5, pady=5)

        # Label để hiển thị kết quả
        self.ketqua_label = ttk.Label(tab1, text="Kết quả: ")
        self.ketqua_label.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        # To-Do List cho Tab 2
        ttk.Label(tab2, text="Nhập công việc của bạn:").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
        
        # Entry để nhập công việc
        self.task_entry = ttk.Entry(tab2, width=40)
        self.task_entry.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)

        # Nút thêm công việc
        ttk.Button(tab2, text="Thêm công việc", command=self.add_task).grid(column=1, row=1, padx=10, pady=5)

        # Listbox để hiển thị công việc
        self.tasks_listbox = tk.Listbox(tab2, width=40, height=10)
        self.tasks_listbox.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        # Nút xóa công việc
        ttk.Button(tab2, text="Xóa công việc", command=self.remove_task).grid(column=0, row=3, columnspan=2, padx=10, pady=5)

    # Hàm xử lý các phép tính
    def cong(self):
        result = self.a.get() + self.b.get()
        self.ketqua_label.config(text=f"Kết quả: {result}")

    def tru(self):
        result = self.a.get() - self.b.get()
        self.ketqua_label.config(text=f"Kết quả: {result}")

    def nhan(self):
        result = self.a.get() * self.b.get()
        self.ketqua_label.config(text=f"Kết quả: {result}")

    def chia(self):
        if self.b.get() != 0:
            result = self.a.get() / self.b.get()
            self.ketqua_label.config(text=f"Kết quả: {result}")
        else:
            self.ketqua_label.config(text="Lỗi: Không thể chia cho 0")

    # Các hàm cho To-Do List
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            msg.showwarning("Cảnh báo", "Vui lòng nhập công việc")

    def remove_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            msg.showwarning("Cảnh báo", "Vui lòng chọn công việc để xóa")

    # Tạo một tab mới không có nội dung
    def create_new_tab(self):
        new_tab = ttk.Frame(self.tabControl)
        tab_name = f"Tab {len(self.tabControl.tabs()) + 1}"
        self.tabControl.add(new_tab, text=tab_name)
    
# Chạy chương trình
if __name__ == "__main__":
    app = OOP()
    app.win.mainloop()