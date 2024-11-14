# Import các lớp và thư viện cần thiết
from models import Database  # Import lớp Database từ models.py để thao tác với cơ sở dữ liệu
from views import LoginView, MainView  # Import các lớp giao diện LoginView và MainView từ views.py
from tkinter import Tk  

# Lớp Controller để điều khiển luồng dữ liệu giữa Model (Database) và View (LoginView, MainView)
class Controller:
    def __init__(self):
        self.database = Database() # Khởi tạo đối tượng Database để kết nối và thao tác với cơ sở dữ liệu
        self.root = Tk()
        self.show_login_view() # Hiển thị giao diện đăng nhập đầu tiên
        self.root.mainloop()   # Bắt đầu vòng lặp chính của tkinter để ứng dụng có thể chạy và hiển thị

    # Hàm xác thực người dùng
    def verify_user(self, username, password):
        # Gọi phương thức verify_user từ lớp Database để kiểm tra thông tin đăng nhập
        return self.database.verify_user(username, password)

    # Hàm hiển thị giao diện đăng nhập
    def show_login_view(self):
        # Khởi tạo LoginView và truyền vào đối tượng root và controller
        LoginView(self.root, self)

    # Hàm hiển thị giao diện chính của ứng dụng sau khi đăng nhập thành công
    def show_main_view(self):
        # Đặt lại cửa sổ root để mở một cửa sổ chính mới và hiển thị MainView
        self.root = Tk()
        MainView(self.root, self)

    # Hàm thêm một lịch hẹn mới vào cơ sở dữ liệu
    def add_appointment(self, name, phone, appointment_date, service):
        # Gọi phương thức add_appointment từ lớp Database
        self.database.add_appointment(name, phone, appointment_date, service)

    # Hàm lấy danh sách tất cả lịch hẹn
    def get_appointments(self):
        # Gọi phương thức get_appointments từ lớp Database và trả về kết quả
        return self.database.get_appointments()

    # Hàm xóa một lịch hẹn dựa trên ID
    def delete_appointment(self, appointment_id):
        # Gọi phương thức delete_appointment từ lớp Database với ID của lịch hẹn cần xóa
        self.database.delete_appointment(appointment_id)


if __name__ == "__main__":
    Controller()