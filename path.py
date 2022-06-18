import osmnx as ox
city = ox.gdf_from_place('New South Wales')
ox.plot_shape(ox.project_gdf(city))