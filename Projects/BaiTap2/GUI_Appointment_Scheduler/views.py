# Import các thư viện cần thiết
from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import DateEntry  # Thư viện để chọn ngày

# Lớp Tooltip 
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        # Gắn các sự kiện để hiển thị và ẩn tooltip
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    # Hàm hiển thị tooltip khi di chuột qua widget
    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        # Tính toán vị trí của tooltip
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        # Tạo cửa sổ tooltip
        self.tip_window = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Loại bỏ viền cửa sổ tooltip
        tw.wm_geometry(f"+{x}+{y}")
        # Thiết lập nội dung và hiển thị tooltip
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("Arial", 10, "normal"))
        label.pack(ipadx=1)

    # Hàm ẩn tooltip khi rời chuột khỏi widget
    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

# Lớp LoginView cho giao diện đăng nhập
class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.setup_ui()  # Gọi hàm thiết lập giao diện đăng nhập

    # Thiết lập giao diện đăng nhập
    def setup_ui(self):
        self.root.title("Login")
        self.root.geometry("400x200")
        self.root.config(bg="#e0f7fa")  # Thiết lập màu nền cho cửa sổ

        # Tạo nhãn và ô nhập cho tên đăng nhập và mật khẩu
        Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=10)
        self.username_entry = Entry(self.root, font=("Arial", 12))
        self.username_entry.pack()

        Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=10)
        self.password_entry = Entry(self.root, font=("Arial", 12), show="*")
        self.password_entry.pack()

        # Nút đăng nhập với sự kiện đăng nhập
        login_btn = Button(self.root, text="Login", font=("Arial", 12), command=self.login)
        login_btn.pack(pady=20)

    # Hàm xử lý sự kiện đăng nhập
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Gọi hàm xác thực từ controller
        if self.controller.verify_user(username, password):
            messagebox.showinfo("Success", "Đăng nhập thành công!")
            self.root.destroy()  # Đóng cửa sổ đăng nhập
            self.controller.show_main_view()  # Hiển thị giao diện chính
        else:
            messagebox.showerror("Error", "Đăng nhập thất bại!") 

# Lớp MainView cho giao diện chính của ứng dụng
class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.setup_ui()  # Thiết lập giao diện chính

    # Hàm thiết lập giao diện chính của ứng dụng
    def setup_ui(self):
        self.root.title("Ứng dụng Đặt Lịch Hẹn")
        self.root.geometry("900x800")
        self.root.config(bg="#e0f7fa")  # Đặt màu nền

        # Tạo tiêu đề cho ứng dụng
        header_label = Label(self.root, text="Đặt Lịch Hẹn", font=("Arial", 24, "bold"), bg="#26c6da", fg="white", pady=15)
        header_label.pack(fill=X)
        Tooltip(header_label, "Đây là phần tiêu đề của ứng dụng đặt lịch hẹn")

        # Tạo khung chính chứa các trường nhập liệu
        main_frame = Frame(self.root, bg="#ffffff", padx=20, pady=20)
        main_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

        # Các trường nhập liệu: tên, số điện thoại, ngày hẹn, và dịch vụ
        Label(main_frame, text="Tên khách hàng:", font=("Arial", 14), bg="#ffffff").grid(row=0, column=0, sticky=W, pady=5)
        self.name_entry = Entry(main_frame, width=35, font=("Arial", 14), relief="solid", bd=1)
        self.name_entry.grid(row=0, column=1, pady=5)
        Tooltip(self.name_entry, "Nhập tên khách hàng")

        Label(main_frame, text="Số điện thoại:", font=("Arial", 14), bg="#ffffff").grid(row=1, column=0, sticky=W, pady=5)
        self.phone_entry = Entry(main_frame, width=35, font=("Arial", 14), relief="solid", bd=1)
        self.phone_entry.grid(row=1, column=1, pady=5)
        Tooltip(self.phone_entry, "Nhập số điện thoại khách hàng")

        Label(main_frame, text="Chọn ngày:", font=("Arial", 14), bg="#ffffff").grid(row=2, column=0, sticky=W, pady=5)
        self.date_entry = DateEntry(main_frame, width=32, font=("Arial", 14), date_pattern="yyyy-mm-dd", relief="solid", bd=1)
        self.date_entry.grid(row=2, column=1, pady=5)
        Tooltip(self.date_entry, "Chọn ngày hẹn")

        Label(main_frame, text="Dịch vụ:", font=("Arial", 14), bg="#ffffff").grid(row=3, column=0, sticky=W, pady=5)
        self.service_entry = Entry(main_frame, width=35, font=("Arial", 14), relief="solid", bd=1)
        self.service_entry.grid(row=3, column=1, pady=5)
        Tooltip(self.service_entry, "Nhập dịch vụ mà khách hàng yêu cầu")

        # Khung chứa các nút chức năng
        button_frame = Frame(main_frame, bg="#ffffff")
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        # Các nút chức năng chính
        button_width = 15
        add_btn = Button(button_frame, text="Thêm lịch hẹn", font=("Arial", 13), command=self.add_appointment, bg="#4CAF50", fg="white", width=button_width)
        add_btn.pack(side=LEFT, padx=5)
        Tooltip(add_btn, "Nhấn vào đây để thêm lịch hẹn")

        edit_btn = Button(button_frame, text="Chỉnh sửa", font=("Arial", 13), command=self.edit_appointment, bg="#FFA726", fg="white", width=button_width)
        edit_btn.pack(side=LEFT, padx=5)
        Tooltip(edit_btn, "Nhấn vào đây để chỉnh sửa lịch hẹn đã chọn")

        delete_btn = Button(button_frame, text="Xóa lịch hẹn", font=("Arial", 13), command=self.delete_appointment, bg="#f44336", fg="white", width=button_width)
        delete_btn.pack(side=LEFT, padx=5)
        Tooltip(delete_btn, "Nhấn vào đây để xóa lịch hẹn đã chọn")

        clear_all_btn = Button(button_frame, text="Xóa tất cả", font=("Arial", 13), command=self.clear_all_appointments, bg="#D32F2F", fg="white", width=button_width)
        clear_all_btn.pack(side=LEFT, padx=5)
        Tooltip(clear_all_btn, "Nhấn vào đây để xóa tất cả lịch hẹn")

        exit_btn = Button(button_frame, text="Thoát", font=("Arial", 13), command=self.exit_app, bg="#9E9E9E", fg="white", width=button_width)
        exit_btn.pack(side=LEFT, padx=5)
        Tooltip(exit_btn, "Thoát ứng dụng")

        # Khung tìm kiếm lịch hẹn
        search_frame = Frame(self.root, bg="#ffffff")
        search_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
        search_label = Label(search_frame, text="Tìm kiếm khách hàng:", font=("Arial", 14), bg="#ffffff")
        search_label.pack(side=LEFT, padx=10)
        self.search_entry = Entry(search_frame, font=("Arial", 14), width=35)
        self.search_entry.pack(side=LEFT, padx=10)
        search_btn = Button(search_frame, text="Tìm kiếm", command=self.search_appointment, font=("Arial", 14), bg="#00796B", fg="white")
        search_btn.pack(side=LEFT, padx=10)
        Tooltip(self.search_entry, "Nhập tên khách hàng cần tìm")

        # Khung và bảng Treeview để hiển thị danh sách lịch hẹn
        tree_frame = Frame(self.root, bg="#ffffff")
        tree_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        tree_label = Label(tree_frame, text="Danh sách lịch hẹn:", font=("Arial", 14), bg="#ffffff")
        tree_label.pack(anchor=W, padx=10, pady=5)

        # Cấu hình bảng Treeview hiển thị danh sách lịch hẹn
        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Tên", "Số điện thoại", "Ngày giờ hẹn", "Dịch vụ"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tên", text="Tên")
        self.tree.heading("Số điện thoại", text="Số điện thoại")
        self.tree.heading("Ngày giờ hẹn", text="Ngày hẹn")
        self.tree.heading("Dịch vụ", text="Dịch vụ")

        # Thiết lập chiều rộng và vị trí các cột
        self.tree.column("ID", width=50, anchor=CENTER)
        self.tree.column("Tên", width=200)
        self.tree.column("Số điện thoại", width=150)
        self.tree.column("Ngày giờ hẹn", width=200)
        self.tree.column("Dịch vụ", width=200)

        # Hiển thị bảng danh sách lịch hẹn
        self.tree.pack(padx=10, pady=5, fill=BOTH, expand=True)
        self.show_appointments()  # Hiển thị dữ liệu từ cơ sở dữ liệu

    # Hàm thêm lịch hẹn mới
    def add_appointment(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        appointment_date = self.date_entry.get_date()
        service = self.service_entry.get()
        if name == "" or phone == "" or service == "":
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
        else:
            try:
                self.controller.add_appointment(name, phone, appointment_date, service)
                messagebox.showinfo("Thành công", "Đã thêm lịch hẹn!")
                self.clear_entries()
                self.show_appointments()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

    # Hàm chỉnh sửa lịch hẹn đã chọn
    def edit_appointment(self):
        try:
            selected_item = self.tree.selection()[0]
            appointment_id = self.tree.item(selected_item)["values"][0]

            # Đưa thông tin lịch hẹn đã chọn vào các trường nhập liệu để chỉnh sửa
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, self.tree.item(selected_item)["values"][1])
            self.phone_entry.delete(0, END)
            self.phone_entry.insert(0, self.tree.item(selected_item)["values"][2])
            self.date_entry.set_date(self.tree.item(selected_item)["values"][3])
            self.service_entry.delete(0, END)
            self.service_entry.insert(0, self.tree.item(selected_item)["values"][4])

            # Nút để lưu các thay đổi
            def save_edits():
                appointment_date = self.date_entry.get_date()
                self.controller.database.update_appointment(appointment_id, self.name_entry.get(), self.phone_entry.get(), appointment_date, self.service_entry.get())
                messagebox.showinfo("Thành công", "Đã cập nhật lịch hẹn!")
                self.clear_entries()
                self.show_appointments()
                save_btn.pack_forget()  # Ẩn nút sau khi lưu

            save_btn = Button(self.root, text="Lưu thay đổi", font=("Arial", 14), command=save_edits, bg="#2196F3", fg="white")
            save_btn.pack(pady=10)
        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn lịch hẹn để chỉnh sửa!")

    # Hàm xóa lịch hẹn đã chọn
    def delete_appointment(self):
        try:
            selected_item = self.tree.selection()[0]
            appointment_id = self.tree.item(selected_item)["values"][0]
            self.controller.delete_appointment(appointment_id)
            messagebox.showinfo("Thành công", "Đã xóa lịch hẹn!")
            self.show_appointments()
        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn lịch hẹn để xóa!")

    # Hàm xóa tất cả lịch hẹn sau khi người dùng xác nhận
    def clear_all_appointments(self):
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa tất cả lịch hẹn?")
        if confirm:
            self.controller.database.clear_all_appointments()
            self.show_appointments()
            messagebox.showinfo("Thành công", "Đã xóa tất cả lịch hẹn!")

    # Hàm thoát ứng dụng với xác nhận
    def exit_app(self):
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát ứng dụng?")
        if confirm:
            self.root.destroy()

    # Hàm hiển thị danh sách lịch hẹn từ cơ sở dữ liệu lên bảng Treeview
    def show_appointments(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = self.controller.get_appointments()
        for row in rows:
            self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3].strftime("%Y-%m-%d"), row[4]))

    # Hàm tìm kiếm lịch hẹn theo tên khách hàng
    def search_appointment(self):
        query = self.search_entry.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = self.controller.database.search_appointments(query)
        for row in rows:
            self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3].strftime("%Y-%m-%d"), row[4]))

    # Hàm xóa nội dung của các trường nhập liệu
    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.service_entry.delete(0, END)