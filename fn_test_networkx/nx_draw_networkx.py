import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

graph_nx = nx.MultiDiGraph()

# Globals.
graph_nx.graph["features"] = np.array([0.6, 0.7, 0.8])
# Nodes.
graph_nx.add_node(0, features=np.array([0.3, 1.3]))
graph_nx.add_node(1, features=np.array([0.4, 1.4]))
graph_nx.add_node(2, features=np.array([0.5, 1.5]))
graph_nx.add_node(3, features=np.array([0.6, 1.6]))
# Edges.
graph_nx.add_edge(0, 1, features=np.array([3.6, 3.7]))
graph_nx.add_edge(2, 0, features=np.array([5.6, 5.7]))
graph_nx.add_edge(3, 0, features=np.array([6.6, 6.7]))

ax = plt.figure(1).gca()

node_labels = {node: "{:.3g}".format(data["features"][0])
                for node, data in graph_nx.nodes(data=True)
                if data["features"] is not None}
edge_labels = {(sender, receiver): "{:.3g}".format(data["features"][0])
                for sender, receiver, data in graph_nx.edges(data=True)
                if data["features"] is not None}
global_label = ("{:.3g}".format(graph_nx.graph["features"][0])
                if graph_nx.graph["features"] is not None else None)

pos = nx.spring_layout(graph_nx)
nx.draw_networkx(graph_nx, pos, ax=ax, labels=node_labels)
nx.draw_networkx_edge_labels(graph_nx, pos, edge_labels, ax=ax)

plt.text(0.05, 0.95, global_label, transform=ax.transAxes)

# ax.yaxis.set_visible(False)
# ax.xaxis.set_visible(False)
plt.show()