from flask import Flask, render_template

app = Flask(__name__, static_folder='E:\\Nam_III\\HK241\\PythonNangCao\\Python_Programming\\TH\\Lab 6\\application\\templates\\static')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)