import requests
import pandas as pd

# API Key của bạn
API_KEY = 'AIzaSyAOXSwWPf-mm1qWt1M-ZQ6LoMwRhiXTm28'

# Các video ID cần truy vấn
video_ids = ['7cmvABXyUC0', '9eH-7x7swEM', 'JndzGxbwvG0', 'l0P5_E6J_g0']

# URL để lấy thông tin video
url = "https://www.googleapis.com/youtube/v3/videos"

# Danh sách để lưu kết quả
items = []

# Lặp qua từng video ID và lấy thông tin
for video_id in video_ids:
    params = {
        'part': 'statistics',
        'id': video_id,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    
    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        data = response.json()
        # Kiểm tra nếu dữ liệu tồn tại
        if 'items' in data and len(data['items']) > 0:
            stats = data['items'][0]['statistics']
            # Lấy thông tin và thêm vào danh sách items
            items.append({
                'videoid': video_id,
                'viewCount': stats.get('viewCount', 0),
                'likeCount': stats.get('likeCount', 0),
                'dislikeCount': stats.get('dislikeCount', 0),
                'favoriteCount': stats.get('favoriteCount', 0),
                'commentCount': stats.get('commentCount', 0)
            })
    else:
        print(f"Lỗi: Không thể lấy thông tin cho video ID {video_id}")

# Chuyển đổi danh sách items thành DataFrame và lưu thành file CSV
fields = ['videoid', 'viewCount', 'likeCount', 'dislikeCount', 'favoriteCount', 'commentCount']
summaryResults = pd.DataFrame(items, columns=fields)
summaryResults.to_csv('video_statistics.csv', index=False)
print("Dữ liệu đã được lưu vào file video_statistics.csv")