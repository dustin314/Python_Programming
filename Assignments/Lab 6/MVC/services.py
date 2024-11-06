from models import User

def get_users():
    users = User.query.all()  # Truy vấn tất cả người dùng từ CSDL
    return users