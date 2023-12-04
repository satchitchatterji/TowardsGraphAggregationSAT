import networkx as nx
import matplotlib.pyplot as plt


def draw_labeled_graph(edge_list, v, savelabel):
    # Create a directed graph from the list of edges
    plt.clf()

    G = nx.DiGraph()
    G.add_edges_from(edge_list)
    G.add_nodes_from([i for i in range(v)])

    # Draw the graph with labels
    pos = nx.spring_layout(G)  # You can choose a different layout if needed
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', arrowsize=15)

    # plt.savefig(f"graphs/{savelabel}.png", bbox_inches="tight")
    plt.show()

# for i in range(2**(v**2)):
# 	print(i)
# 	graph = get_graph(i, v)
# 	draw_labeled_graph(graph, v, i)
# 	# print(graph)