import urllib.request
import re
import os

# URL của trang web cần phân tích
url = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages/"

# Tạo thư mục "images" nếu chưa tồn tại
if not os.path.exists("images"):
    os.makedirs("images")

# Tải nội dung HTML của trang
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

# Sử dụng regular expression để tìm tất cả các đường dẫn ảnh trong trang
image_urls = re.findall(r'src="([^"]+\.png)"', html)

# Lặp qua từng URL hình ảnh và tải về
for image_url in image_urls:
    # Nếu đường dẫn không chứa URL đầy đủ, bổ sung phần URL chính
    if not image_url.startswith("http"):
        image_url = urllib.parse.urljoin(url, image_url)
    
    # Lấy tên file từ URL
    file_name = image_url.split("/")[-1]
    
    # Đường dẫn lưu file trong thư mục "images"
    save_path = os.path.join("images", file_name)
    
    # Tải và lưu ảnh
    urllib.request.urlretrieve(image_url, save_path)
    print(f"Tải thành công {file_name} vào thư mục 'images'")

print("Hoàn thành tải tất cả các ảnh.")