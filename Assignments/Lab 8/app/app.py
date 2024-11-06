from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mail import Mail, Message
from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime
from werkzeug.utils import secure_filename
from math import ceil
from markdown import markdown
import bleach
from uuid import uuid4
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Thêm cấu hình thư mục tải lên
UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Cấu hình email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cgkiet314@gmail.com'
app.config['MAIL_PASSWORD'] = 'Kietchau3124'
app.config['MAIL_DEFAULT_SENDER'] = 'cgkiet314@gmail.com'

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.secret_key)

# Giả lập database người dùng
USERS = {
    'cgkiet314@gmail.com': {
        'password': '1234',
        'name': 'Kiệt',
        'confirmed': True,
        'profile': {
            'full_name': 'Châu Gia Kiệt',
            'location': 'TP HCM',
            'bio': 'Sinh Viên Văn Lang',
            'join_date': '2017-07-23',
            'avatar': None,
            'website': 'https://example.com',
            'github': 'dustin',
            'twitter': 'dustin'
        }
    }
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def send_confirmation_email(email):
    token = serializer.dumps(email, salt='email-confirm')
    confirm_url = url_for('confirm_email', token=token, _external=True)
    
    msg = Message('Confirm Your Account', recipients=[email])
    msg.html = render_template('confirm.html', confirm_url=confirm_url)
    mail.send(msg)

@app.route('/')
@login_required
def home():
    user = USERS[session['user']['email']]
    if not user['confirmed']:
        return redirect(url_for('unconfirmed'))
    return render_template('home.html', name=user['name'])

@app.route('/auth/unconfirmed')
@login_required
def unconfirmed():
    user = USERS[session['user']['email']]
    if user['confirmed']:
        return redirect(url_for('home'))
    return render_template('unconfirmed.html', name=user['name'])

@app.route('/auth/confirm/<token>')
def confirm_email(token):
    try:
        email = serializer.loads(token, salt='email-confirm', max_age=3600)
    except:
        flash('The confirmation link is invalid or has expired.')
        return redirect(url_for('login'))
    
    user = USERS.get(email)
    if user:
        if user['confirmed']:
            flash('Account already confirmed. Please login.')
        else:
            user['confirmed'] = True
            flash('You have confirmed your account. Thanks!')
    
    return redirect(url_for('login'))

@app.route('/auth/resend')
@login_required
def resend_confirmation():
    user = USERS[session['user']['email']]
    if user['confirmed']:
        flash('Your account is already confirmed.')
        return redirect(url_for('home'))
    
    send_confirmation_email(session['user']['email'])
    flash('A new confirmation email has been sent.')
    return redirect(url_for('unconfirmed'))

# Route đăng nhập
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in USERS and USERS[email]['password'] == password:
            # Thêm vai trò vào session (giả sử 'admin' hoặc 'user')
            session['user'] = {
                'email': email,
                'name': USERS[email]['name'],
                'role': 'admin'  # Thêm role ở đây (đặt là 'admin' hoặc 'user' tuỳ vào logic của bạn)
            }
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if email in USERS:
            flash('Email already registered')
        elif password != confirm_password:
            flash('Passwords do not match')
        elif len(password) < 6:
            flash('Password must be at least 6 characters long')
        else:
            USERS[email] = {
                'password': password,
                'name': username,
                'confirmed': False,
                'profile': {
                    'full_name': username,
                    'location': '',
                    'bio': '',
                    'join_date': datetime.now().strftime('%Y-%m-%d')
                }
            }
            session['user'] = {
                'email': email,
                'name': username
            }
            send_confirmation_email(email)
            return redirect(url_for('unconfirmed'))
        
        return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/profile')
@login_required
def view_profile():
    email = session.get('user', {}).get('email')
    user = USERS.get(email)

    if not user:
        flash('User not found!')
        return redirect(url_for('home'))

    if not user['confirmed']:
        return redirect(url_for('unconfirmed'))

    return render_template('profile.html', user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    email = session.get('user', {}).get('email')
    if not email:
        flash('Please log in to access this page.')
        return redirect(url_for('login'))
    
    user = USERS[email]

    if request.method == 'POST':
        # Cập nhật thông tin cơ bản
        user['profile']['full_name'] = request.form['full_name']
        user['profile']['location'] = request.form['location']
        user['profile']['bio'] = request.form['bio']
        
        # Kiểm tra và xử lý file avatar nếu có tải lên
        if 'avatar' in request.files:
            avatar = request.files['avatar']
            if avatar and allowed_file(avatar.filename):
                # Tạo tên file an toàn
                filename = secure_filename(avatar.filename)
                # Lưu file vào thư mục upload
                avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Cập nhật tên file vào profile của người dùng
                user['profile']['avatar'] = filename
        
        flash('Profile updated successfully!')
        return redirect(url_for('view_profile'))

    return render_template('edit_profile.html', user=user)

# Danh sách bài đăng blog (dữ liệu tạm thời trong bộ nhớ)
BLOG_POSTS = []
COMMENTS = []

# Số bài đăng trên mỗi trang
POSTS_PER_PAGE = 5

@app.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    if request.method == 'POST':
        content = request.form.get('content')
        is_comment = request.form.get('is_comment') == 'true'

        if content:
            if is_comment:
                # Thêm bình luận mới chưa được phê duyệt
                comment = {
                    'id': str(uuid4()),
                    'username': session['user']['name'],
                    'content': content,
                    'timestamp': datetime.now(),
                    'approved': False  # Mặc định là chưa được duyệt
                }
                COMMENTS.insert(0, comment)
                flash("Your comment has been added and is pending approval.")
            else:
                # Thêm bài đăng mới
                html_content = markdown(content)
                safe_content = bleach.clean(html_content, tags=[
                    'b', 'i', 'u', 'em', 'strong', 'a', 'h1', 'h2', 'h3', 'p', 'ul', 'ol', 'li', 'br'
                ], attributes={'a': ['href', 'title']})
                
                post = {
                    'username': session['user']['name'],
                    'content': safe_content,
                    'timestamp': datetime.now()
                }
                BLOG_POSTS.insert(0, post)
                flash("Your post has been published.")
                
            return redirect(url_for('blog'))
        else:
            flash("Content cannot be empty.")

    # Lấy tất cả bình luận, bao gồm cả bình luận chưa được duyệt
    page = request.args.get('page', 1, type=int)
    total_posts = len(BLOG_POSTS)
    total_pages = ceil(total_posts / POSTS_PER_PAGE)
    start = (page - 1) * POSTS_PER_PAGE
    end = start + POSTS_PER_PAGE
    posts = BLOG_POSTS[start:end]  # Lấy bài đăng cho trang hiện tại

    return render_template('blog.html', posts=posts, comments=COMMENTS, page=page, total_pages=total_pages)


# Route AJAX để phê duyệt bình luận
@app.route('/approve_comment', methods=['POST'])
@login_required
def approve_comment():
    comment_id = request.json.get('comment_id')
    for comment in COMMENTS:
        if comment['id'] == comment_id:
            comment['approved'] = True
            return jsonify({"success": True, "message": "Comment approved.", "approved": True})
    return jsonify({"success": False, "message": "Comment not found."}), 404

@app.route('/reject_comment', methods=['POST'])
@login_required
def reject_comment():
    comment_id = request.json.get('comment_id')
    for comment in COMMENTS:
        if comment['id'] == comment_id:
            comment['approved'] = False
            return jsonify({"success": True, "message": "Comment rejected.", "approved": False})
    return jsonify({"success": False, "message": "Comment not found."}), 404



# Route để xóa bình luận
@app.route('/delete_comment/<comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    global COMMENTS
    COMMENTS = [comment for comment in COMMENTS if comment['id'] != comment_id or comment['username'] != session['user']['name']]
    flash("Comment deleted.")
    return redirect(url_for('blog'))

# Route để chỉnh sửa bình luận
@app.route('/edit_comment/<comment_id>', methods=['GET', 'POST'])
@login_required
def edit_comment(comment_id):
    comment = next((c for c in COMMENTS if c['id'] == comment_id and c['username'] == session['user']['name']), None)
    
    if not comment:
        flash("Comment not found or you don't have permission to edit this comment.")
        return redirect(url_for('blog'))

    if request.method == 'POST':
        new_content = request.form.get('content')
        if new_content:
            comment['content'] = new_content
            flash("Comment updated.")
            return redirect(url_for('blog'))
        else:
            flash("Content cannot be empty.")

    return render_template('edit_comment.html', comment=comment)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)