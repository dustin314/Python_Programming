from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Book, User, Rental
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# Cấu hình Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route hiển thị danh sách sách
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Route thêm sách mới
@app.route('/add', methods=['POST'])
@login_required
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    published_year = request.form.get('published_year')
    description = request.form.get('description')
    
    new_book = Book(title=title, author=author, published_year=published_year, description=description)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('index'))

# Route xóa sách
@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('index'))

# Route hiển thị form chỉnh sửa sách
@app.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit_book(id):
    book = Book.query.get(id)
    return render_template('edit.html', book=book)

# Route cập nhật sách
@app.route('/update/<int:id>', methods=['POST'])
@login_required
def update_book(id):
    book = Book.query.get(id)
    if book:
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.published_year = request.form.get('published_year')
        book.description = request.form.get('description')
        
        db.session.commit()
    return redirect(url_for('index'))

# Route đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Kiểm tra người dùng đã tồn tại
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Tên người dùng hoặc email đã tồn tại.')
            return redirect(url_for('register'))

        # Tạo người dùng mới
        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Đăng ký thành công. Hãy đăng nhập.')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        # Kiểm tra thông tin đăng nhập
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Đăng nhập thành công.')
            return redirect(url_for('index'))
        else:
            flash('Tên người dùng hoặc mật khẩu không chính xác.')

    return render_template('login.html')

# Route đăng xuất
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bạn đã đăng xuất.')
    return redirect(url_for('login'))

# Route hiển thị danh sách sách để thuê
@app.route('/rent_books')
@login_required
def rent_books():
    # Lọc ra các sách chưa có bản ghi Rental với return_date là None (chưa được thuê)
    available_books = Book.query.outerjoin(Rental).filter(
        (Rental.id == None) | (Rental.return_date != None)
    ).all()
    return render_template('rent_books.html', books=available_books)

# Route để thuê sách
@app.route('/rent/<int:book_id>', methods=['POST'])
@login_required
def rent(book_id):
    book = Book.query.get(book_id)
    if not book:
        flash('Book not found.')
        return redirect(url_for('rent_books'))

    rental = Rental(user_id=current_user.id, book_id=book.id)
    db.session.add(rental)
    db.session.commit()
    flash('You have successfully rented the book.')
    return redirect(url_for('my_rentals'))

# Route để hiển thị sách đã thuê của người dùng
@app.route('/my_rentals')
@login_required
def my_rentals():
    # Truy vấn sách mà người dùng hiện tại đang thuê
    rentals = Rental.query.filter_by(user_id=current_user.id, return_date=None).all()
    return render_template('my_rentals.html', rentals=rentals)

# Route trả sách
@app.route('/return/<int:rental_id>', methods=['POST'])
@login_required
def return_book(rental_id):
    rental = Rental.query.get(rental_id)
    if rental and rental.user_id == current_user.id and rental.return_date is None:
        rental.return_date = datetime.utcnow()
        db.session.commit()
        flash('Trả sách thành công!')
    else:
        flash('Có lỗi xảy ra khi trả sách.')
    return redirect(url_for('my_rentals'))


if __name__ == "__main__":
    app.run(debug=True)