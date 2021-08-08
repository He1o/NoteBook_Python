import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1, features = 10)
G.add_node(1, features = 20)
G.add_node(2, features = 'bobo')

nodes = [(3, {'features' : 'aoao'}), (4, {'features' : 9})]
G.add_nodes_from(nodes)

G.nodes[1]['features'] = 'nice'
print(G.nodes)
print(G.nodes(data = True))

G.add_edge(0, 1, distance = 100)
G.add_edge(0, 1, distance = 200)

edges = [(1, 3, {'distance': 142}), (2, 3, {'distance': 19})]
G.add_edges_from(edges)

G.edges[0, 1]['distance'] = 999
G[0][1]['distance'] = 1999

print(G.edges)
print(G.edges(data = True))


for n in G.neighbors(1):
    print(n)
for n in G[1]:
    print(n)
for nbr, datadict in G.adj[2].items():
    print(nbr, datadict)
for nbr, datadict in G[2].items():
    print(nbr, datadict)
print(G.has_node(0))
print(G.has_node(5))
print(G.has_edge(0,1))
print(G.has_edge(2,1))

for node_index, node_feature in G.nodes(data=True):
    print(node_index, node_feature)
for receiver, sender, features in G.edges(data=True):
    print(receiver, sender, features)

diG = G.to_directed()
for receiver, sender, features in diG.edges(data=True):
    print(receiver, sender, features)
diG = nx.DiGraph(G)
