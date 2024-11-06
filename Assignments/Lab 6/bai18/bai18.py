from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  

class DienTenForm(FlaskForm):
    ten = StringField('Tên bạn là gì?', validators=[DataRequired()])
    nut_guilenserver = SubmitField('Gửi')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DienTenForm()
    if form.validate_on_submit():
        ten = form.ten.data
        flash(f'Chào {ten}!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)