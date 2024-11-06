import requests

# Thiết lập tham số lat và lon
parameters = {"lat": 37.78, "lon": -122.41}

# Gọi API và lấy kết quả trả về từ URL mới của NASA
response = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "DEMO_KEY"})

# Kiểm tra mã trạng thái phản hồi
if response.status_code == 200:
    try:
        json_data = response.json()
        print("Loại dữ liệu:", type(json_data))
        print("Dữ liệu trả về:", json_data)

        # Kiểm tra nếu dữ liệu có trường duration
        if "duration" in json_data:
            first_duration = json_data['duration']
            print("Duration:", first_duration)
        else:
            print("Trường 'duration' không có trong dữ liệu trả về.")
    except requests.exceptions.JSONDecodeError:
        print("Lỗi: Không thể phân tích dữ liệu JSON")
else:
    print(f"Lỗi: Mã trạng thái phản hồi là {response.status_code}")
    print("Nội dung phản hồi:", response.text)