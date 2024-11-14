from app import app, db
from models import User

with app.app_context():
    # Khởi tạo đối tượng User với tên người dùng là 'admin'
    user = User(username="admin")
    
    # Đặt mật khẩu cho người dùng bằng cách sử dụng phương thức set_password của lớp User
    user.set_password("123456")
    
    # Thêm người dùng mới vào phiên làm việc của SQLAlchemy
    db.session.add(user)
    # Ghi thay đổi vào cơ sở dữ liệu để lưu người dùng mới
    db.session.commit()
    
    # In ra thông báo xác nhận người dùng đã được tạo thành công
    print("Người dùng 'admin' đã được tạo thành công!")
