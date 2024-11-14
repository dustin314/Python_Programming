from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash  # Thư viện bảo mật mật khẩu
from flask_sqlalchemy import SQLAlchemy  # Thư viện ORM của Flask để làm việc với cơ sở dữ liệu
from flask_login import UserMixin 

# Khởi tạo đối tượng cơ sở dữ liệu
db = SQLAlchemy()

# Định nghĩa lớp User, đại diện cho bảng 'users' trong cơ sở dữ liệu
class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Tên bảng
    id = db.Column(db.Integer, primary_key=True)  # Khóa chính cho bảng
    username = db.Column(db.String(50), unique=True, nullable=False)  # Tên người dùng, duy nhất và không được để trống
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email, duy nhất và không được để trống
    password = db.Column(db.String(200), nullable=False)  # Mật khẩu, được lưu trữ dưới dạng hash
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Ngày tạo, tự động lấy thời gian hiện tại

    # Phương thức thiết lập mật khẩu với mã hóa
    def set_password(self, password):
        self.password = generate_password_hash(password)  # Hash mật khẩu và lưu vào thuộc tính password

    # Phương thức kiểm tra mật khẩu
    def check_password(self, password):
        return check_password_hash(self.password, password)  # So sánh mật khẩu nhập vào với hash đã lưu

# Định nghĩa lớp Book, đại diện cho bảng 'books' trong cơ sở dữ liệu
class Book(db.Model):
    __tablename__ = 'books'  # Tên bảng
    id = db.Column(db.Integer, primary_key=True)  # Khóa chính cho bảng
    title = db.Column(db.String(120), nullable=False)  # Tên sách, không được để trống
    author = db.Column(db.String(120), nullable=False)  # Tác giả, không được để trống
    published_year = db.Column(db.Integer, nullable=False)  # Năm xuất bản, không được để trống
    description = db.Column(db.Text)  # Mô tả sách

# Định nghĩa lớp Rental, đại diện cho bảng 'rentals' trong cơ sở dữ liệu
class Rental(db.Model):
    __tablename__ = 'rentals'  # Tên bảng 
    id = db.Column(db.Integer, primary_key=True)  # Khóa chính cho bảng
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Khóa ngoại liên kết đến bảng 'users'
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)  # Khóa ngoại liên kết đến bảng 'books'
    rental_date = db.Column(db.DateTime, default=datetime.utcnow)  # Ngày thuê sách, mặc định là thời gian hiện tại
    return_date = db.Column(db.DateTime, nullable=True)  # Ngày trả sách, có thể để trống nếu chưa trả

    # Thiết lập mối quan hệ với User và Book
    user = db.relationship('User', backref='rentals')  # Liên kết với User, giúp truy vấn ngược các bản ghi thuê
    book = db.relationship('Book', backref='rentals')  # Liên kết với Book, giúp truy vấn ngược các bản ghi thuê