from app import app, db
from models import User

# Tạo người dùng mẫu trong ngữ cảnh ứng dụng
with app.app_context():
    # Tạo người dùng mẫu
    user = User(username="admin")
    user.set_password("123456")  # Đặt mật khẩu cho người dùng
    db.session.add(user)
    db.session.commit()
    print("Người dùng 'admin' đã được tạo thành công!")