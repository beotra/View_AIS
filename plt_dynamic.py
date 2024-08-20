



# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from matplotlib.animation import FuncAnimation
# import numpy as np
# import matplotlib.patheffects as PathEffects

# csv_file = 'C:/Users/ASUS/Desktop/DOAN/View_AIS/01_08.csv'
# df = pd.read_csv(csv_file)

# df['# Timestamp'] = pd.to_datetime(df['# Timestamp'], format='%d/%m/%Y %H:%M:%S')

# start_time = df['# Timestamp'].min()
# end_time = df['# Timestamp'].max()

# mmsi_list = df['MMSI'].unique()
# cmap = plt.get_cmap('Dark2')

# # Lấy danh sách các màu từ colormap
# colors = cmap(np.linspace(0, 1, cmap.N))
# np.random.shuffle(colors)
# mmsi_color_map = {mmsi: colors[i % len(colors)] for i, mmsi in enumerate(mmsi_list)}

# # Tạo figure và axes
# fig, ax = plt.subplots(figsize=(10*927/777,10))

# # Đọc và hiển thị ảnh nền
# img = mpimg.imread('C:/Users/ASUS/Desktop/DOAN/map.png')  # Thay thế đường dẫn với file ảnh của bạn
# image_extent = [11, 13, 53.9, 54.9]  # [xmin, xmax, ymin, ymax]

# # Hiển thị ảnh nền
# ax.imshow(img, extent=image_extent, origin='upper', aspect='auto')

# # Cài đặt giới hạn cho axes
# ax.set_xlim(11, 13)
# ax.set_ylim(53.9, 54.9)
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# ax.set_title('AIS Data Visualization')

# # Tạo từ điển lưu các đối tượng mũi tên
# scatters = {mmsi: None for mmsi in mmsi_list}
# selected_mmsi = None  # MMSI của mũi tên đang được chọn

# # Hàm xử lý sự kiện khi click vào mũi tên
# def on_click(event):
#     global selected_mmsi

#     for mmsi, arrow in scatters.items():
#         if arrow is not None:
#             contains, _ = arrow.contains(event)
#             if contains:
#                 print(f'Bạn đã click vào tàu có MMSI: {mmsi}')

#                 # Đặt viền màu vàng cho mũi tên được chọn
#                 arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
#                                         PathEffects.Normal()])

#                 # Quay lại viền bình thường cho mũi tên trước đó
#                 if selected_mmsi and selected_mmsi != mmsi:
#                     scatters[selected_mmsi].set_path_effects([])

#                 selected_mmsi = mmsi
#                 fig.canvas.draw()
#                 break

# # Hàm cập nhật dữ liệu và biểu đồ
# def update(frame):
#     current_time = start_time + pd.Timedelta(minutes=frame * 10)
#     current_data = df[df['# Timestamp'] <= current_time]

#     for mmsi, color in mmsi_color_map.items():
#         data_mmsi = current_data[current_data['MMSI'] == mmsi]

#         # Xóa mũi tên cũ
#         if scatters[mmsi] is not None:
#             scatters[mmsi].remove()

#         if not data_mmsi.empty:
#             latest_data = data_mmsi.iloc[-1]
            
#             #cog_rad = np.deg2rad(latest_data['COG'])
#             goc=latest_data['COG']

#             arrow = ax.text(
#                 latest_data['Longitude'], latest_data['Latitude'],
#                 '➤',
#                 color=color,
#                 fontsize=12,
#                 ha='center',
#                 va='center',
#                 #rotation=np.rad2deg(cog_rad)+90,  # Xoay mũi tên theo COG
#                 #rotation=goc+90,
#                 rotation=90-goc,
#                 rotation_mode='anchor'
#             )

#             # Nếu mũi tên này là mũi tên đã được chọn, giữ viền màu vàng
#             if mmsi == selected_mmsi:
#                 arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
#                                         PathEffects.Normal()])

#             # Lưu mũi tên vào từ điển
#             scatters[mmsi] = arrow

#     return list(scatters.values())

# # Kết nối sự kiện click với hàm on_click
# fig.canvas.mpl_connect('button_press_event', on_click)

# # Hàm khởi tạo animation
# def init():
#     return []

# # Tạo animation
# ani = FuncAnimation(fig, update, frames=int((end_time - start_time).total_seconds() // 600 + 1),
#                     init_func=init, blit=False, repeat=False, interval=1000)

# # Hiển thị biểu đồ
# plt.show()










# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from matplotlib.animation import FuncAnimation
# import numpy as np
# import matplotlib.patheffects as PathEffects

# # Đọc dữ liệu
# csv_file = 'C:/Users/ASUS/Desktop/DOAN/View_AIS/01_08.csv'
# df = pd.read_csv(csv_file)

# df['# Timestamp'] = pd.to_datetime(df['# Timestamp'], format='%d/%m/%Y %H:%M:%S')

# start_time = df['# Timestamp'].min()
# end_time = df['# Timestamp'].max()

# mmsi_list = df['MMSI'].unique()
# cmap = plt.get_cmap('Dark2')

# # Lấy danh sách các màu từ colormap
# colors = cmap(np.linspace(0, 1, cmap.N))
# np.random.shuffle(colors)
# mmsi_color_map = {mmsi: colors[i % len(colors)] for i, mmsi in enumerate(mmsi_list)}

# # Tạo figure và axes cho bản đồ chính
# fig, ax = plt.subplots(figsize=(10*927/777,10))

# # Đọc và hiển thị ảnh nền
# img = mpimg.imread('C:/Users/ASUS/Desktop/DOAN/map.png')  # Thay thế đường dẫn với file ảnh của bạn
# image_extent = [11, 13, 53.9, 54.9]  # [xmin, xmax, ymin, ymax]

# # Hiển thị ảnh nền
# ax.imshow(img, extent=image_extent, origin='upper', aspect='auto')

# # Cài đặt giới hạn cho axes
# ax.set_xlim(11, 13)
# ax.set_ylim(53.9, 54.9)
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# ax.set_title('AIS Data Visualization')

# # Tạo từ điển lưu các đối tượng mũi tên
# scatters = {mmsi: None for mmsi in mmsi_list}
# selected_mmsi = None  # MMSI của mũi tên đang được chọn

# # Tạo figure và axes cho biểu đồ chi tiết tàu
# fig_detail, ax_detail = plt.subplots(figsize=(10, 6))
# ax_detail.set_title('Ship Details')
# ax_detail.set_xlabel('Time')
# ax_detail.set_ylabel('COG / SOG')

# # Hàm xử lý sự kiện khi click vào mũi tên
# def on_click(event):
#     global selected_mmsi

#     for mmsi, arrow in scatters.items():
#         if arrow is not None:
#             contains, _ = arrow.contains(event)
#             if contains:
#                 print(f'Bạn đã click vào tàu có MMSI: {mmsi}')

#                 # Lấy thông tin chi tiết của tàu
#                 info = df[df['MMSI'] == mmsi].tail(5)  # Lấy 5 điểm dữ liệu mới nhất

#                 # Vẽ biểu đồ chi tiết COG và SOG theo thời gian cho 5 điểm dữ liệu mới nhất
#                 ax_detail.clear()  # Xóa biểu đồ cũ
#                 ax_detail.plot(info['Longitude'], info['Latitude'],  color='blue', marker='o')
#                 ax_detail.set_title(f'Ship Details for MMSI: {mmsi} (Last 5 Points)')
#                 fig_detail.canvas.draw()  # Vẽ lại biểu đồ

#                 # Đặt viền màu vàng cho mũi tên được chọn
#                 arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
#                                         PathEffects.Normal()])

#                 # Quay lại viền bình thường cho mũi tên trước đó
#                 if selected_mmsi and selected_mmsi != mmsi:
#                     scatters[selected_mmsi].set_path_effects([])

#                 selected_mmsi = mmsi
#                 fig.canvas.draw()
#                 break

# # Hàm cập nhật dữ liệu và biểu đồ
# def update(frame):
#     current_time = start_time + pd.Timedelta(minutes=frame * 10)
#     current_data = df[df['# Timestamp'] <= current_time]

#     for mmsi, color in mmsi_color_map.items():
#         data_mmsi = current_data[current_data['MMSI'] == mmsi]

#         # Xóa mũi tên cũ
#         if scatters[mmsi] is not None:
#             scatters[mmsi].remove()

#         if not data_mmsi.empty:
#             latest_data = data_mmsi.iloc[-1]
            
#             goc = latest_data['COG']

#             arrow = ax.text(
#                 latest_data['Longitude'], latest_data['Latitude'],  # Chỉnh sửa LON, LAT theo dữ liệu của bạn
#                 '➤',
#                 color=color,
#                 fontsize=12,
#                 ha='center',
#                 va='center',
#                 rotation=90 - goc,
#                 rotation_mode='anchor'
#             )

#             # Nếu mũi tên này là mũi tên đã được chọn, giữ viền màu vàng
#             if mmsi == selected_mmsi:
#                 arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
#                                         PathEffects.Normal()])

#             # Lưu mũi tên vào từ điển
#             scatters[mmsi] = arrow

#     return list(scatters.values())

# # Kết nối sự kiện click với hàm on_click
# fig.canvas.mpl_connect('button_press_event', on_click)

# # Hàm khởi tạo animation
# def init():
#     return []

# # Tạo animation
# ani = FuncAnimation(fig, update, frames=int((end_time - start_time).total_seconds() // 600 + 1),
#                     init_func=init, blit=False, repeat=False, interval=1000)

# # Hiển thị biểu đồ
# plt.show()








import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.patheffects as PathEffects
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Bidirectional, GRU, Dense 
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
from sklearn.cluster import DBSCAN
from dtw import dtw

model = load_model("latlon_50.h5", custom_objects={'mse': MeanSquaredError()})

# Đọc dữ liệu
csv_file = '01_08.csv'
df = pd.read_csv(csv_file)
df=df.dropna(subset=['Longitude', 'Latitude', 'COG', 'SOG'])
df['# Timestamp'] = pd.to_datetime(df['# Timestamp'], format='%d/%m/%Y %H:%M:%S')
start_time = df['# Timestamp'].min()
end_time = df['# Timestamp'].max()

mmsi_list = df['MMSI'].unique()
cmap = plt.get_cmap('Dark2')
colors = cmap(np.linspace(0, 1, cmap.N))
np.random.shuffle(colors)
mmsi_color_map = {mmsi: colors[i % len(colors)] for i, mmsi in enumerate(mmsi_list)}

# Tạo cửa sổ chính
root = tk.Tk()
root.title("AIS Data Visualization")

# Khung bên trái cho biểu đồ
left_frame = tk.Frame(root, width=800, height=600)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Khung bên phải cho các thành phần giao diện
right_frame = tk.Frame(root, width=400, height=600, bg='lightblue')
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Khung cho biểu đồ chi tiết và các thành phần khác trong right_frame
right_frame_top = tk.Frame(right_frame, bg='lightblue')
right_frame_top.pack(side=tk.TOP, fill=tk.X)

right_frame_bottom = tk.Frame(right_frame, bg='lightblue')
right_frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Tạo figure và axes cho biểu đồ chính
fig_main = Figure(figsize=(8, 6))
ax_main = fig_main.add_subplot(111)

# Đọc và hiển thị ảnh nền
img = mpimg.imread('map.png')
image_extent = [11, 13, 53.9, 54.9]
ax_main.imshow(img, extent=image_extent, origin='upper', aspect='auto')
ax_main.set_xlim(11, 13)
ax_main.set_ylim(53.9, 54.9)
ax_main.set_xlabel('Longitude')
ax_main.set_ylabel('Latitude')
ax_main.set_title('AIS Data Visualization')

# Tạo annotation cho thông tin tàu
annotation = None

# Hàm cập nhật biểu đồ chi tiết
def update_detail_plot(mmsi, current_time):
    # Lấy thông tin chi tiết của tàu
    info = df[(df['MMSI'] == mmsi) & (df['# Timestamp'] <= current_time)].tail(6)
    longitude = info['Longitude'].values
    latitude = info['Latitude'].values
    ais_data = []
    for lon, lat in zip(longitude, latitude):
        if len(ais_data)==5:
            break 
        ais_data.append([lon, lat])

    if len(info) > 5:
        input_data = np.array(ais_data)
        test_data = np.expand_dims(input_data, axis=0)
        predictions = model.predict(test_data)
        predicted_point = predictions[0]
        actual_point = ais_data[-1]
        
            # Cập nhật biểu đồ chi tiết
        ax_detail.clear()
        ax_detail.plot(info['Longitude'].iloc[0:5], info['Latitude'].iloc[0:5], color='blue', marker='o')
        ax_detail.plot(info['Longitude'].iloc[-1], info['Latitude'].iloc[-1], color='orange', marker='o')
        ax_detail.plot(predicted_point[0], predicted_point[1], color='green', marker='o')
        # ax_detail.set_xlim(min(info['Longitude'].min(), predicted_point[1]), max(info['Longitude'].max(), predicted_point[1]))
        # ax_detail.set_ylim(min(info['Latitude'].min(), predicted_point[0]), max(info['Latitude'].max(), predicted_point[0]))
        ax_detail.set_title(f'MMSI: {mmsi} (Last 5 Points)')
        # ax_detail.set_xlim(11, 13)
        # ax_detail.set_ylim(53.9, 54.9)
        fig_detail.canvas.draw()
    else:    
        # Cập nhật biểu đồ chi tiết
        ax_detail.clear()
        ax_detail.plot(info['Longitude'], info['Latitude'], color='blue', marker='o')
        ax_detail.set_title(f'MMSI: {mmsi} (Last 5 Points)')
        # ax_detail.set_xlim(11, 13)
        # ax_detail.set_ylim(53.9, 54.9)
        fig_detail.canvas.draw()

# Hàm xử lý sự kiện khi click vào mũi tên
# def on_click(event):
#     global selected_mmsi, annotation

#     # Xóa annotation cũ nếu tồn tại
#     if annotation:
#         annotation.remove()

#     for mmsi, arrow in scatters.items():
#         if arrow is not None:
#             contains, _ = arrow.contains(event)
#             if contains:
#                 print(f'Bạn đã click vào tàu có MMSI: {mmsi}')

#                 # Cập nhật biểu đồ chi tiết
#                 update_detail_plot(mmsi, start_time)

#                 # Đặt viền màu vàng cho mũi tên được chọn
#                 arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
#                                         PathEffects.Normal()])

#                 # Quay lại viền bình thường cho mũi tên trước đó
#                 if selected_mmsi and selected_mmsi != mmsi:
#                     scatters[selected_mmsi].set_path_effects([])

#                 selected_mmsi = mmsi
#                 fig_main.canvas.draw()
                
#                 fields = ['MMSI', 'IMO', 'Callsign', 'Name', 'Ship type', 'Cargo type', 'Width', 'Length',
#                           'Type of position fixing device', 'Draught', 'Destination', 'ETA']
#                 for item in table.get_children():
#                     table.delete(item)
#                 for index, field in enumerate(fields):
#                     value = df[df['MMSI'] == mmsi].iloc[0].get(field, 'N/A')
#                     table.insert('', 'end', values=(index + 1, field, value))    
#                 break


def on_click(event):
    global selected_mmsi, annotation

    # Xóa annotation cũ nếu tồn tại
    if annotation:
        annotation.remove()

    clicked_on_ship = False

    for mmsi, arrow in scatters.items():
        if arrow is not None:
            contains, _ = arrow.contains(event)
            if contains:
                clicked_on_ship = True
                print(f'Bạn đã click vào tàu có MMSI: {mmsi}')

                # Cập nhật biểu đồ chi tiết
                update_detail_plot(mmsi, start_time)

                # Đặt viền màu vàng cho mũi tên được chọn
                arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
                                        PathEffects.Normal()])

                # Quay lại viền bình thường cho mũi tên trước đó
                if selected_mmsi and selected_mmsi != mmsi:
                    scatters[selected_mmsi].set_path_effects([])

                selected_mmsi = mmsi
                fig_main.canvas.draw()
                
                # Hiển thị fig_detail
                canvas_detail_widget.pack(fill=tk.BOTH, expand=True)
                
                fields = ['MMSI', 'IMO', 'Callsign', 'Name', 'Ship type', 'Cargo type', 'Width', 'Length',
                          'Type of position fixing device', 'Draught', 'Destination', 'ETA']
                for item in table.get_children():
                    table.delete(item)
                for index, field in enumerate(fields):
                    value = df[df['MMSI'] == mmsi].iloc[0].get(field, 'N/A')
                    table.insert('', 'end', values=(index + 1, field, value))    
                break

    if not clicked_on_ship:
        # Ẩn fig_detail nếu không click vào tàu
        canvas_detail_widget.pack_forget()

# # Hàm cập nhật dữ liệu và biểu đồ chính
def update(frame):
    current_time = start_time + pd.Timedelta(minutes=frame * 10)
    current_data = df[df['# Timestamp'] <= current_time]

    for mmsi, color in mmsi_color_map.items():
        data_mmsi = current_data[current_data['MMSI'] == mmsi]

        if scatters[mmsi] is not None:
            scatters[mmsi].remove()

        if not data_mmsi.empty:
            latest_data = data_mmsi.iloc[-1]
            goc = latest_data['COG']

            arrow = ax_main.text(
                latest_data['Longitude'], latest_data['Latitude'],
                '➤',
                color=color,
                fontsize=12,
                ha='center',
                va='center',
                rotation=90 - goc,
                rotation_mode='anchor'
            )

            if mmsi == selected_mmsi:
                arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
                                        PathEffects.Normal()])

            scatters[mmsi] = arrow

            # Cập nhật biểu đồ chi tiết nếu tàu đã chọn đang có dữ liệu mới
            if selected_mmsi == mmsi:
                update_detail_plot(mmsi, current_time)

    return list(scatters.values())
# def update(frame):
#     current_time = start_time + pd.Timedelta(minutes=frame * 10)
#     current_data = df[df['# Timestamp'] <= current_time]

#     for mmsi, color in mmsi_color_map.items():
#         data_mmsi = current_data[current_data['MMSI'] == mmsi]

#         if mmsi in scatters:
#             if scatters[mmsi] is not None:
#                 scatters[mmsi].remove()

#         if not data_mmsi.empty:
#             latest_data = data_mmsi.iloc[-1]
#             latitude = latest_data['Latitude']
#             longitude = latest_data['Longitude']
#             goc = latest_data['COG']

#             # Kiểm tra xem tàu có nằm trong vùng biển không
#             if 53.91 <= latitude <= 54.89 and 11.01 <= longitude <= 12.99:
#                 arrow = ax_main.text(
#                     longitude, latitude,
#                     '➤',
#                     color=color,
#                     fontsize=12,
#                     ha='center',
#                     va='center',
#                     rotation=90 - goc,
#                     rotation_mode='anchor'
#                 )

#                 if mmsi == selected_mmsi:
#                     arrow.set_path_effects([PathEffects.Stroke(linewidth=3, foreground='yellow'),
#                                             PathEffects.Normal()])

#                 scatters[mmsi] = arrow

#                 # Cập nhật biểu đồ chi tiết nếu tàu đã chọn đang có dữ liệu mới
#                 if selected_mmsi == mmsi:
#                     update_detail_plot(mmsi, current_time)
#             else:
#                 # Nếu tàu ra ngoài vùng biển, xóa khỏi scatters
#                 if mmsi in scatters:
#                     scatters[mmsi] = None

#     return list(scatters.values())

#các sự kiện thành phần của khung 
def on_combobox_select(event):
    selected_option = combobox.get()
    if selected_option == "Satellite Map":
        img = mpimg.imread('map_vetinh.png')
        image_extent = [11, 13, 53.9, 54.9]
        ax_main.imshow(img, extent=image_extent, origin='upper', aspect='auto')
        # Thêm mã để cập nhật bản đồ vệ tinh
    elif selected_option == "Standard Map":
        img = mpimg.imread('map_diahinh.png')
        image_extent = [11, 13, 53.9, 54.9]
        ax_main.imshow(img, extent=image_extent, origin='upper', aspect='auto')
        # Thêm mã để cập nhật bản đồ thông thường
    elif selected_option == "White Background":
        img = mpimg.imread('map_white.png')
        image_extent = [11, 13, 53.9, 54.9]
        ax_main.imshow(img, extent=image_extent, origin='upper', aspect='auto')

# Khởi tạo scatter dictionary và selected_mmsi
scatters = {mmsi: None for mmsi in mmsi_list}
selected_mmsi = None

# Kết nối sự kiện click với hàm on_click
fig_main.canvas = FigureCanvasTkAgg(fig_main, master=left_frame)
fig_main.canvas_widget = fig_main.canvas.get_tk_widget()
fig_main.canvas_widget.pack(fill=tk.BOTH, expand=True)
fig_main.canvas.draw()
fig_main.canvas.mpl_connect('button_press_event', on_click)

# Hàm khởi tạo animation
def init():
    return []


# Tạo animation cho biểu đồ chính
ani_main = FuncAnimation(fig_main, update, frames=int((end_time - start_time).total_seconds() // 600 + 1),
                         init_func=init, blit=False, repeat=False, interval=1000)

# Tạo figure và axes cho biểu đồ chi tiết
fig_detail = Figure(figsize=(4, 3))
fig_detail.patch.set_facecolor('lightblue')  # Đặt màu nền cho Figure chi tiết
ax_detail = fig_detail.add_subplot(111)
ax_detail.set_facecolor('white')  # Đặt màu nền cho axes chi tiết là trắng
ax_detail.set_xlim(11, 13)
ax_detail.set_ylim(53.9, 54.9)

# Tích hợp biểu đồ chi tiết vào khung bên dưới
canvas_detail = FigureCanvasTkAgg(fig_detail, master=right_frame_bottom)
canvas_detail_widget = canvas_detail.get_tk_widget()
canvas_detail_widget.pack(fill=tk.BOTH, expand=True)

# Thêm các thành phần giao diện vào khung bên trên
button = tk.Button(right_frame_top, text="Sample Button")
button.pack(pady=10, padx=10, anchor='w')

combobox = ttk.Combobox(right_frame_top, values=["Satellite Map", "Standard Map", "White Background"])
combobox.pack(pady=10, padx=10, anchor='w')
combobox.set("Standard Map")
combobox.bind("<<ComboboxSelected>>", on_combobox_select)




# Khung cho table (có thể thêm nội dung vào sau)

columns = ('Index', 'Feature', 'Value')
table = ttk.Treeview(right_frame_top, columns=columns, show='headings')
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)
table.pack(pady=10, padx=10, anchor='w')
# Hiển thị cửa sổ chính
root.mainloop()


#https://www.mdpi.com/2079-9292/13/1/98 mai đọc phân loại tàu bằng phương pháp này 