from axioms import *
from config import *
from explain import *
from literals import *
from properties import *
from utils import *




if __name__ == "__main__":
    graphs = generate_graph_subsets([cnfIrreflexivity, cnfTransitivity, cnfCompleteness])
    config.update_graphs(graphs)

    

    match = 0
    mismatch = 0
    duplicates = 0

    all_graphs = []
    print(config.graphs)
    for g in config.graphs:
        g_dec = get_graph(g, config.v)
        g_dec.sort() # since this is order-invariant anyway, sort to alter test for duplicates

        print(g_dec)
        if g_dec in all_graphs:
            duplicates += 1

        all_graphs.append(g_dec)

    #print(f"{match} MATCHES, {mismatch} MISMATCHES")
    print(f"{duplicates} DECODED DUPLICATES")