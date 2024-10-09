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
        file_menu.add_command(label="New") # Tạo thêm file mới 
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
        tabControl = ttk.Notebook(self.win)

        # Tab 1 
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab1')

        # Tab 2
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Tab2')

        tabControl.pack(expand=1, fill='both')

# Chạy chương trình
if __name__ == "__main__":
    app = OOP()
    app.win.mainloop()
