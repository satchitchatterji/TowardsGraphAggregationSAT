from config import *

def allVoters():
    return range(n)

def allVertices():
    return range(v)

def allGraphs():
    return range(g)

def allEdges():
    return range(e)


def graphCNF(G_edges):
    cnf = []
    for x in allVertices():
        for y in allVertices():
            if (x,y) in G_edges:
                cnf.append((posEdgeLiteral(x,y),))
            else:
                cnf.append((negEdgeLiteral(x,y),))
    return cnf

def get_edge_xy(edge_int, v):
    assert 1<=v<v**2
    return divmod(edge_int, v)

def get_graph(graph_int, v):
    assert graph_int < 2**(v**2)
    n_edges = v**2
    max_bin_rep = len(bin(n_edges)[2:])
    binary_repr = str(bin(graph_int))[2:]
    binary_repr = "0"*(max_bin_rep-len(binary_repr))+binary_repr
    edges = [get_edge_xy(i,v) for i, digit in enumerate(reversed(binary_repr)) if digit=="1"]
    return edges


def complete():
    cnf = []
    for x in allVertices():
        for y in allVertices():
            if x!=y:
                cnf.append((posEdgeLiteral(x,y), posEdgeLiteral(y,x)))
    return cnf