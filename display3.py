# import pandas as pd
# import folium
# from folium.plugins import TimestampedGeoJson
# from flask import Flask, request, jsonify
# import os

# app = Flask(__name__)

# # Đường dẫn tới tệp CSV và HTML
# csv_file = 'test_data.csv'
# html_file = os.path.join('static', 'ship_map.html')  # Lưu vào thư mục static của Flask

# # Hàm tạo bản đồ từ tệp CSV
# def create_map(csv_file, html_file):
#     print(f"Creating map from {csv_file} and saving to {html_file}")
#     df = pd.read_csv(csv_file)
#     df['# Timestamp'] = pd.to_datetime(df['# Timestamp'])
#     df = df.sort_values(by='# Timestamp')

#     m = folium.Map(location=[df['Latitude'].iloc[0], df['Longitude'].iloc[0]], zoom_start=2)

#     features = []
#     for idx, row in df.iterrows():
#         feature = {
#             'type': 'Feature',
#             'geometry': {
#                 'type': 'Point',
#                 'coordinates': [row['Longitude'], row['Latitude']],
#             },
#             'properties': {
#                 'time': row['# Timestamp'].isoformat(),
#                 'popup': f"{row['MMSI']} ({row['# Timestamp']})"
#             }
#         }
#         features.append(feature)

#     geojson = {
#         'type': 'FeatureCollection',
#         'features': features
#     }

#     TimestampedGeoJson(
#         geojson,
#         period='PT1M',
#         add_last_point=True,
#     ).add_to(m)

#     m.save(html_file)
#     print(f"Map saved to {html_file}")

# # Tạo bản đồ lần đầu tiên khi khởi động server
# if not os.path.exists(html_file):
#     create_map(csv_file, html_file)

# @app.route('/add_data', methods=['POST'])
# def add_data():
#     data = request.json
#     new_row = pd.DataFrame([data])

#     # Thêm dữ liệu mới vào tệp CSV
#     new_row.to_csv(csv_file, mode='a', header=False, index=False)

#     # Tạo lại bản đồ với dữ liệu mới
#     create_map(csv_file, html_file)

#     return jsonify({"status": "success", "message": "Data added and map updated."})

# @app.route('/')
# def index():
#     return f'<a href="/static/ship_map.html">View Map</a>'  # Sử dụng URL tới bản đồ trong thư mục static

# if __name__ == '__main__':
#     app.run(debug=True)



#phiên bản 2
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
from flask import Flask, request, jsonify
import os
import schedule
import time

app = Flask(__name__)

# Đường dẫn tới tệp CSV và HTML
csv_file = 'test_data.csv'
html_file = 'ship_map.html'

# Hàm tạo bản đồ từ tệp CSV
def create_map(csv_file, html_file):
    print(f"Creating map from {csv_file} and saving to {html_file}")
    df = pd.read_csv(csv_file)
    df['# Timestamp'] = pd.to_datetime(df['# Timestamp'])
    df = df.sort_values(by='# Timestamp')

    # Tạo đối tượng bản đồ
    m = folium.Map(location=[df['Latitude'].iloc[0], df['Longitude'].iloc[0]], zoom_start=2)

    # Tạo danh sách các MMSI duy nhất để phân nhóm dữ liệu
    unique_mmsi = df['MMSI'].unique()

    # Tạo màu sắc ngẫu nhiên cho mỗi MMSI
    import random
    colors = {mmsi: "#{:06x}".format(random.randint(0, 0xFFFFFF)) for mmsi in unique_mmsi}

    features = []
    for idx, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['Longitude'], row['Latitude']],
            },
            'properties': {
                'time': row['# Timestamp'].isoformat(),
                'popup': f"{row['MMSI']} ({row['# Timestamp']})"
            },
            'style': {
                'color': colors[row['MMSI']],
                'fillColor': colors[row['MMSI']],
                'fillOpacity': 0.5,
                'weight': 2,
                'radius': 8
            }
        }
        features.append(feature)

    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    # Thêm TimestampedGeoJson vào bản đồ
    TimestampedGeoJson(
        geojson,
        period='PT1M',  # Khoảng thời gian giữa các điểm
        add_last_point=True,
    ).add_to(m)

    # Lưu bản đồ vào file HTML
    m.save(html_file)
    print(f"Map saved to {html_file}")

# Hàm cập nhật bản đồ và thêm dữ liệu mới mỗi 3 giây
def update_map_schedule():
    create_map(csv_file, html_file)

# Lập lịch cho hàm cập nhật
schedule.every(3).seconds.do(update_map_schedule)

# Tạo bản đồ lần đầu tiên khi khởi động server
if not os.path.exists(html_file):
    create_map(csv_file, html_file)

# Hàm chạy lặp để duy trì lập lịch
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    new_row = pd.DataFrame([data])

    # Thêm dữ liệu mới vào tệp CSV
    new_row.to_csv(csv_file, mode='a', header=False, index=False)

    return jsonify({"status": "success", "message": "Data added."})

@app.route('/')
def index():
    return f'<a href="static/ship_map.html">View Map</a>'

if __name__ == '__main__':
    # Bắt đầu lập lịch và chạy server Flask
    run_schedule()
    app.run(debug=True)
