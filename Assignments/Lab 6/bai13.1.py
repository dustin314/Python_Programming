from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Lấy file từ form có input name là 'the_file'
        f = request.files['the_file']
        # Lưu file vào đường dẫn chỉ định
        f.save('/var/www/uploads/uploaded_file.txt')
        return 'File đã được upload thành công!'
    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="the_file">
        <input type="submit">
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)