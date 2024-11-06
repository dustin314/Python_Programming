from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    if not username:
        username = 'Guest'
    
    return f'Hello, {username}!'

@app.route('/set_cookie')
def set_cookie():
    resp = make_response(render_template_string('<h1>Cookie đã được đặt!</h1>'))
    resp.set_cookie('username', 'FlaskUser')
    
    return resp

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response(render_template_string('<h1>Cookie đã bị xóa!</h1>'))
    resp.set_cookie('username', '', expires=0)
    return resp


if __name__ == '__main__':
    app.run(debug=True)