import osmnx as ox
import networkx as nx

G = ox.graph_from_address('广州大学', dist=6000, network_type='all')  # 第一步，获取道路数据
ox.plot_graph(G)
origin_point = (23.039506, 113.364664)  # 广州大学校门坐标
destination_point = (23.074058, 113.386148)  # 中山大学校门坐标
origin_node = ox.nearest_nodes(G, origin_point[1], origin_point[0])  # 获取O最邻近的道路节点
destination_node = ox.nearest_nodes(G, destination_point[1], destination_point[0])  # 获取D最邻近的道路节点
route = nx.shortest_path(G, origin_node, destination_node, weight='length')  # 请求获取最短路径
distance = nx.shortest_path_length(G, origin_node, destination_node, weight='length')  # 并获取路径长度
fig, ax = ox.plot_graph_route(G, route)  # 可视化结果
print(str(distance))  # 输出最短路径距离 作者：没书读的铁憨憨 https://www.bilibili.com/read/cv13578508 出处：bilibili