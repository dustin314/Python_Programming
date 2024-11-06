from urllib.request import urlopen
import csv

# URL của dữ liệu
url = 'http://sixty-north.com/c/t.txt'

# Đọc dữ liệu từ URL và lưu vào danh sách lstStory
with urlopen(url) as story:
    lstStory = story.readlines()

# Tạo và ghi dữ liệu vào tệp CSV
with open('story.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Ghi từng dòng vào file CSV
    for line in lstStory:
        # Chuyển đổi dòng từ bytes sang chuỗi và loại bỏ ký tự xuống dòng
        writer.writerow([line.decode('utf-8').strip()])

print("Đã lưu dữ liệu vào tệp story.csv")