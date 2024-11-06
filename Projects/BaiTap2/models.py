# Import các thư viện cần thiết
import psycopg2 
from tkinter import messagebox 
from datetime import datetime  # Thư viện làm việc với đối tượng ngày và giờ

# Lớp Database dùng để quản lý kết nối và thao tác với cơ sở dữ liệu
class Database:
    def __init__(self):
        # Khởi tạo kết nối đến cơ sở dữ liệu và con trỏ để thực hiện các câu truy vấn SQL
        self.conn = self.connect_to_db()
        self.c = self.conn.cursor()

    # Hàm kết nối đến cơ sở dữ liệu PostgreSQL
    def connect_to_db(self):
        try:
            conn = psycopg2.connect(
                dbname="dbtest",       
                user="postgres",       
                password="123456",      
                host="localhost",       
                port="5432"             
            )
            return conn
        except Exception as e:
            # Nếu kết nối thất bại, hiển thị thông báo lỗi
            messagebox.showerror("Lỗi", f"Không thể kết nối đến cơ sở dữ liệu!\n{e}")
            return None

    # Hàm thêm lịch hẹn mới vào cơ sở dữ liệu
    def add_appointment(self, name, phone, appointment_date, service):
        try:
            # Thực hiện truy vấn thêm dữ liệu vào bảng `appointments`
            self.c.execute("INSERT INTO appointments (name, phone, appointment_date, service) VALUES (%s, %s, %s, %s)",
                           (name, phone, appointment_date, service))
            self.conn.commit()  # Xác nhận thay đổi trong cơ sở dữ liệu
        except Exception as e:
            # Nếu có lỗi, hủy thay đổi và ném ra ngoại lệ
            self.conn.rollback()
            raise e

    # Hàm lấy danh sách tất cả các lịch hẹn từ cơ sở dữ liệu
    def get_appointments(self):
        self.c.execute("SELECT * FROM appointments")  # Truy vấn tất cả các lịch hẹn
        return self.c.fetchall()  # Trả về kết quả truy vấn dưới dạng danh sách

    # Hàm xóa một lịch hẹn dựa trên ID
    def delete_appointment(self, appointment_id):
        self.c.execute("DELETE FROM appointments WHERE id=%s", (appointment_id,)) # Thực hiện truy vấn xóa lịch hẹn với ID cụ thể
        self.conn.commit()  # Xác nhận thay đổi trong cơ sở dữ liệu

    # Hàm cập nhật thông tin lịch hẹn dựa trên ID
    def update_appointment(self, appointment_id, name, phone, appointment_date, service):
        # Truy vấn cập nhật thông tin lịch hẹn với các giá trị mới
        self.c.execute("UPDATE appointments SET name=%s, phone=%s, appointment_date=%s, service=%s WHERE id=%s",
                       (name, phone, appointment_date, service, appointment_id))
        self.conn.commit()  # Xác nhận thay đổi

    # Hàm tìm kiếm lịch hẹn theo tên khách hàng
    def search_appointments(self, query):
        # Truy vấn tìm kiếm lịch hẹn có tên chứa chuỗi `query`
        self.c.execute("SELECT * FROM appointments WHERE name ILIKE %s", ('%' + query + '%',))
        return self.c.fetchall()  # Trả về kết quả truy vấn

    # Hàm xóa tất cả các lịch hẹn trong bảng
    def clear_all_appointments(self):
        self.c.execute("DELETE FROM appointments") 
        self.conn.commit()  # Xác nhận thay đổi trong cơ sở dữ liệu

    # Hàm xác thực người dùng
    def verify_user(self, username, password):
        # Tên đăng nhập và mật khẩu
        return username == "admin" and password == "1234"

    # Hàm đóng kết nối với cơ sở dữ liệu
    def close_connection(self):
        self.conn.close() 