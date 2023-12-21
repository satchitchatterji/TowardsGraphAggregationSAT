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
    internal_mismatch = 0

    i = 1
    for E in allProfiles():
        #print("Profile", E)
        for x in allVertices():
            for y in allVertices():
                lit = posLiteral(E,x,y)
                edgelit_dec = toEdgeLiteral(lit)[0]
                edge_lit = posEdgeLiteral(x,y)
                if edge_lit == edgelit_dec:
                    match += 1
                else:
                    mismatch += 1
                
                if edge_lit != i or edgelit_dec != i:
                    print(edge_lit, edgelit_dec,i)
                    internal_mismatch += 1
                    
                i += 1

        i = 1

    print(f"{match} MATCHES, {mismatch} MISMATCHES")
    print(f"{internal_mismatch} DUPLICATES IN ONE SET")