import osmnx as ox
G = ox.graph_from_address(address="天津大学, 天津市, 中国", dist=1000, dist_type="bbox",network_type='drive')
ox.plot_graph(G)