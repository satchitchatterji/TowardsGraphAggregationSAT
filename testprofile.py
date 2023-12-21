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

    for g in graphs:
        gr = profileIntToProfile(g)
        g_recon = profileToProfileInt(gr)

        if g == g_recon:
            match += 1
        else:
            mismatch += 1
            print(g, "\n\n", g_recon)


    print(f"{match} MATCHES, {mismatch} MISMATCHES")