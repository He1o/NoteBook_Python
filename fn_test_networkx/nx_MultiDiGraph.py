import networkx as nx
import numpy as np

graph_nx = nx.MultiDiGraph()

# Globals.
graph_nx.graph["features"] = np.array([0.6, 0.7, 0.8])
print(graph_nx.graph)
# Nodes.
graph_nx.add_node(0, features=np.array([0.3, 1.3]))
graph_nx.add_node(1, features=np.array([0.4, 1.4]))
graph_nx.add_node(2, features=np.array([0.5, 1.5]))
graph_nx.add_node(3, features=np.array([0.6, 1.6]))
print(graph_nx.nodes)
print(graph_nx.nodes[1]['features'])
print(graph_nx.nodes(data=True))  #return all the attributes
# Edges.
graph_nx.add_edge(0, 1, features=np.array([3.6, 3.7]))
graph_nx.add_edge(2, 0, features=np.array([5.6, 5.7]))
graph_nx.add_edge(3, 0, features=np.array([6.6, 6.7]))
print(graph_nx.edges)
print(graph_nx[0][1][0]['features'])  #the third subscrip is the number of edges
print(graph_nx.edges[0, 1, 0]['features'])  #the third subscrip is the number of edges
print(graph_nx[0])  # {1: {0: {'features': array([3.6, 3.7])}}}

for i,j in graph_nx.edges():
    graph_nx.add_edge(1,0, dis =1)


