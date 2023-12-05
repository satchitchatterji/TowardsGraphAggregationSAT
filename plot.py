import networkx as nx
import matplotlib.pyplot as plt
from utils import get_graph

def draw_labeled_graph(edge_list, v, plot=True, savelabel=""):
    # Create a directed graph from the list of edges
    plt.clf()

    G = nx.DiGraph()
    G.add_edges_from(edge_list)
    G.add_nodes_from([i for i in range(v)])

    # Draw the graph with labels
    pos = nx.spring_layout(G)  # You can choose a different layout if needed
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', arrowsize=15)

    if savelabel != "":
        plt.savefig(f"graphs/{savelabel}.png", bbox_inches="tight")
    if plot:
        plt.show()

    return 


def draw_profile(graphs, v, winner_graph):
    n_players = len(graphs)
    for graph in graphs:
        


# for i in [1,2,3,4]:
# 	print(i)
# 	graph = get_graph(i, v)
# 	draw_labeled_graph(graph, v, i)
# 	# print(graph)