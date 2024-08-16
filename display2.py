import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson

# Đọc tệp CSV
filename = 'test_data.csv'
df = pd.read_csv(filename)

# Hiển thị dữ liệu
print(df.head(5))

# Sắp xếp dữ liệu theo cột thời gian (giả sử cột thời gian là 'MMSI')
df['# Timestamp'] = pd.to_datetime(df['# Timestamp'])  # Chuyển đổi cột thời gian thành kiểu datetime nếu chưa
df = df.sort_values(by='# Timestamp')  # Sắp xếp dữ liệu theo cột thời gian

# Tạo đối tượng bản đồ trung tâm tại vị trí đầu tiên trong tệp CSV
m = folium.Map(location=[df['Latitude'].iloc[0], df['Longitude'].iloc[0]], zoom_start=2)

# Tạo danh sách các điểm dữ liệu với thông tin cần thiết
features = []
for idx, row in df.iterrows():
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['Longitude'], row['Latitude']],
        },
        'properties': {
            '# Timestamp': row['# Timestamp'].isoformat(),
            'popup': f"{row['MMSI']} ({row['# Timestamp']})"
        }
    }
    features.append(feature)

# Tạo đối tượng GeoJson với các điểm dữ liệu
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
m.save('ship_map.html')

print("Bản đồ đã được lưu vào file ship_map.html")