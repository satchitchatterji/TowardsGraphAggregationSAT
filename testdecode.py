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
                edgelit_dec = toLiteral(posEdgeLiteral(x,y), E)[0]
                lit = posLiteral(E,x,y)
                if edgelit_dec == lit:
                    match += 1
                else:
                    mismatch += 1
                
                if lit != i or edgelit_dec != i:
                    internal_mismatch += 1
                i += 1

    print(f"{match} MATCHES, {mismatch} MISMATCHES")
    print(f"{internal_mismatch} DUPLICATES IN ONE SET")