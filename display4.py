import geopandas as gpd

# Đọc dữ liệu từ bộ dữ liệu ví dụ của GeoPandas
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

# Tạo cột Hemisphere
gdf['Hemisphere'] = gdf['geometry'].apply(lambda x: 'Norte' if x.y > 0 else 'Sur')

# Tạo cột Color
gdf['Color'] = gdf['Hemisphere'].apply(lambda x: '#D94325' if x == 'Norte' else '#5CD925')

# Sử dụng hàm explore để trực quan hóa
gdf.explore(column='Hemisphere', color=gdf['Color'])
