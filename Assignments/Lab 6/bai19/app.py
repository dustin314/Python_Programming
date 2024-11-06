from flask import Flask, render_template, flash, redirect, url_for
from hello import NameForm  # Import form từ tệp hello.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        flash(f'Hello, {name}!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)