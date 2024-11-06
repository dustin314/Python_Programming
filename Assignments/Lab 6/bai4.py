from flask import Flask 

ungdung = Flask(__name__)

@ungdung.route('/')
def hello():
    tentruong = 'Dai hoc Van Lang!'
    lienket = '<a href="https://www.vanlanguni.edu.vn">' + tentruong + '</a><br>'
    chuoi = lienket
    import datetime
    nam = datetime.date.today().year
    chuoi = chuoi + '<b>Xin<i>chao</i>Tan sinh vien nam ' + str(nam) + '!</b>'
    return chuoi 


if __name__ == "__main__":
    ungdung.run()