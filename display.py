import pandas as pd
import folium

# Đọc tệp CSV
filename = 'ship_positions.csv'
df = pd.read_csv(filename)

# Hiển thị dữ liệu
print(df)

# Tạo đối tượng bản đồ trung tâm tại vị trí đầu tiên trong tệp CSV
m = folium.Map(location=[df['lat'][0], df['lng'][0]], zoom_start=2)

# Thêm các điểm dữ liệu vào bản đồ
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['lat'], row['lng']],
        popup=f"{row['name']} ({row['time']})",
    ).add_to(m)

# Lưu bản đồ vào file HTML
m.save('ship_map.html')

print("Bản đồ đã được lưu vào file ship_map.html")