# Import các thư viện cần thiết
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash 
from models import db, Book, User, Rental  
from config import Config 
from flask_migrate import Migrate  # Thư viện di chuyển cơ sở dữ liệu khi có thay đổi
from flask_login import LoginManager, login_user, logout_user, login_required, current_user  # Để quản lý đăng nhập
from werkzeug.security import generate_password_hash, check_password_hash  # Bảo mật mật khẩu

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config.from_object(Config)  # Áp dụng cấu hình từ file Config
db.init_app(app)  # Khởi tạo kết nối cơ sở dữ liệu với ứng dụng Flask
migrate = Migrate(app, db)  # Cấu hình Flask-Migrate để hỗ trợ cập nhật cơ sở dữ liệu

# Cấu hình Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)  # Kết nối login_manager với ứng dụng Flask
login_manager.login_view = 'login'  # Trang đăng nhập mặc định nếu người dùng chưa đăng nhập

# Hàm tải người dùng từ ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Lấy người dùng theo ID từ cơ sở dữ liệu

# Route hiển thị danh sách sách
@app.route('/')
def index():
    books = Book.query.all()  # Lấy tất cả các sách từ cơ sở dữ liệu
    return render_template('index.html', books=books)  # Trả về trang index hiển thị danh sách sách

# Route thêm sách mới, yêu cầu người dùng đăng nhập
@app.route('/add', methods=['POST'])
@login_required
def add_book():
    # Lấy thông tin sách từ form
    title = request.form.get('title')
    author = request.form.get('author')
    published_year = request.form.get('published_year')
    description = request.form.get('description')
    
    # Tạo đối tượng sách mới và thêm vào cơ sở dữ liệu
    new_book = Book(title=title, author=author, published_year=published_year, description=description)
    db.session.add(new_book)
    db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    return redirect(url_for('index'))  # Chuyển hướng về trang chủ

# Route xóa sách, yêu cầu người dùng đăng nhập
@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_book(id):
    book = Book.query.get(id)  # Lấy sách theo ID
    if book:
        db.session.delete(book)  # Xóa sách khỏi cơ sở dữ liệu
        db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    return redirect(url_for('index'))  # Quay lại trang chủ

# Route hiển thị form chỉnh sửa sách, yêu cầu người dùng đăng nhập
@app.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit_book(id):
    book = Book.query.get(id)  # Lấy sách cần chỉnh sửa
    return render_template('edit.html', book=book)  # Trả về trang chỉnh sửa sách

# Route cập nhật thông tin sách sau khi chỉnh sửa, yêu cầu người dùng đăng nhập
@app.route('/update/<int:id>', methods=['POST'])
@login_required
def update_book(id):
    book = Book.query.get(id)  # Lấy sách cần cập nhật
    if book:
        # Cập nhật thông tin sách từ form
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.published_year = request.form.get('published_year')
        book.description = request.form.get('description')
        
        db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    return redirect(url_for('index'))  # Quay lại trang chủ

# Route đăng ký người dùng mới
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Lấy thông tin đăng ký từ form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Kiểm tra người dùng đã tồn tại
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Tên người dùng hoặc email đã tồn tại.') 
            return redirect(url_for('register'))  # Quay lại trang đăng ký

        # Tạo người dùng mới và thêm vào cơ sở dữ liệu
        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
        flash('Đăng ký thành công. Hãy đăng nhập.') 
        return redirect(url_for('login'))  # Chuyển hướng đến trang đăng nhập

    return render_template('register.html')  # Hiển thị trang đăng ký

# Route đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lấy thông tin đăng nhập từ form
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()  # Tìm người dùng theo tên đăng nhập

        # Kiểm tra mật khẩu
        if user and check_password_hash(user.password, password):
            login_user(user)  # Đăng nhập người dùng
            flash('Đăng nhập thành công.') 
            return redirect(url_for('index'))  # Chuyển hướng về trang chủ
        else:
            flash('Tên người dùng hoặc mật khẩu không chính xác.')

    return render_template('login.html')  # Hiển thị trang đăng nhập

# Route đăng xuất, yêu cầu người dùng đăng nhập
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Đăng xuất người dùng
    flash('Bạn đã đăng xuất.') 
    return redirect(url_for('login'))  # Quay lại trang đăng nhập

# Route hiển thị sách có thể thuê, yêu cầu người dùng đăng nhập
@app.route('/rent_books')
@login_required
def rent_books():
    # Lọc ra các sách chưa có bản ghi Rental với return_date là None (chưa được thuê)
    available_books = Book.query.outerjoin(Rental).filter(
        (Rental.id == None) | (Rental.return_date != None)
    ).all()
    return render_template('rent_books.html', books=available_books)  # Hiển thị trang sách có sẵn để thuê

# Route thuê sách, yêu cầu người dùng đăng nhập
@app.route('/rent/<int:book_id>', methods=['POST'])
@login_required
def rent(book_id):
    book = Book.query.get(book_id)  # Lấy sách theo ID
    if not book:
        flash('Không tìm thấy sách.') 
        return redirect(url_for('rent_books'))  # Quay lại trang thuê sách

    # Tạo bản ghi thuê sách và thêm vào cơ sở dữ liệu
    rental = Rental(user_id=current_user.id, book_id=book.id)
    db.session.add(rental)
    db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    flash('Bạn đã thuê sách thành công.') 
    return redirect(url_for('my_rentals'))  # Chuyển hướng đến trang sách đã thuê

# Route hiển thị danh sách sách mà người dùng đã thuê
@app.route('/my_rentals')
@login_required
def my_rentals():
    # Truy vấn sách mà người dùng hiện tại đang thuê
    rentals = Rental.query.filter_by(user_id=current_user.id, return_date=None).all()
    return render_template('my_rentals.html', rentals=rentals)  # Hiển thị danh sách sách đã thuê

# Route trả sách, yêu cầu người dùng đăng nhập
@app.route('/return/<int:rental_id>', methods=['POST'])
@login_required
def return_book(rental_id):
    rental = Rental.query.get(rental_id)  # Lấy bản ghi thuê sách
    # Kiểm tra nếu bản ghi đúng người dùng và chưa được trả
    if rental and rental.user_id == current_user.id and rental.return_date is None:
        rental.return_date = datetime.utcnow()  # Cập nhật ngày trả sách
        db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
        flash('Trả sách thành công!') 
    else:
        flash('Có lỗi xảy ra khi trả sách.') 
    return redirect(url_for('my_rentals'))  # Quay lại trang sách đã thuê



if __name__ == "__main__":
    app.run(debug=True)  