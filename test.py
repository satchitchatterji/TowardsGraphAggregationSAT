import networkx as nx
import matplotlib.pyplot as plt

def get_edge_xy(edge_int, v):
	assert v>1
	return divmod(edge_int, v)

def get_graph(graph_int, v):
	assert graph_int <= 2**(v**2)
	n_edges = v**2
	max_bin_rep = len(bin(n_edges)[2:])
	binary_repr = str(bin(graph_int))[2:]
	binary_repr = "0"*(max_bin_rep-len(binary_repr))+binary_repr
	edges = [get_edge_xy(i,v) for i, digit in enumerate(reversed(binary_repr)) if digit=="1"]
	return edges

v = 2
for i in range(2**(v**2)):
	graph = get_graph(i, v)
	print(graph)

# def draw_labeled_graph(edge_list, v, savelabel):
#     # Create a directed graph from the list of edges
#     plt.clf()

#     G = nx.DiGraph()
#     G.add_edges_from(edge_list)
#     G.add_nodes_from([i for i in range(v)])

#     # Draw the graph with labels
#     pos = nx.spring_layout(G)  # You can choose a different layout if needed
#     nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', arrowsize=15)

#     plt.savefig(f"graphs/{savelabel}.png", bbox_inches="tight")

# for i in range(2**(v**2)):
# 	print(i)
# 	graph = get_graph(i, v)
# 	draw_labeled_graph(graph, v, i)
# 	# print(graph)