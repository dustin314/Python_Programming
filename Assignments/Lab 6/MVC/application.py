from flask import Flask, render_template
from services import get_users
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    users = get_users()  # Gọi hàm từ services
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)