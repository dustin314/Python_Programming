from flask import Flask, session, redirect, url_for, request
from markupsafe import escape 

app = Flask(__name__)

app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {escape(session["username"])}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)