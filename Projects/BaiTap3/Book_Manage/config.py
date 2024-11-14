import os

# Đặt đường dẫn thư mục gốc của dự án
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Lấy đường dẫn tuyệt đối của thư mục chứa file hiện tại

class Config:
    # Khóa bí mật của ứng dụng Flask dùng cho bảo mật (như mã hóa session)
    SECRET_KEY = '73cdcb13b533e923f8e32a7586971c3f'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/dbbook'
    # Tắt tính năng theo dõi các thay đổi trong SQLAlchemy để giảm thiểu tài nguyên hệ thống
    SQLALCHEMY_TRACK_MODIFICATIONS = False