from flask import Flask, request

app = Flask(__name__)

@app.route('/timkiem', methods=['GET', 'POST'])
def tim_kiem():
    if request.method == 'POST':
        # Xử lý khi POST (người dùng nhấn nút tìm kiếm)
        noidung_cantim = request.form.get('txtnoidung', '')
        return f'Kết quả tìm kiếm cho: {noidung_cantim}'
    # Khi GET (người dùng mở trang lần đầu)
    return '''
    <form method="post">
        Nội dung cần tìm: <input type="text" name="txtnoidung">
        <input type="submit" value="Tìm kiếm">
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)