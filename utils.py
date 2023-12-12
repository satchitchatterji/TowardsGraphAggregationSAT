from config import config
from literals import (
    posEdgeLiteral,
    negEdgeLiteral
)

from functools import lru_cache

from itertools import permutations

############################
# "ALL" Functions
############################


def allVoters():
    return range(config.n)

def allVertices():
    return range(config.v)

def allGraphs():
    return range(config.g)

def allEdges():
    return range(config.e)

def allProfiles():
    return range(config.r)


#################################
# CNF Generation
#################################

def graphCNF(G_edges):
    """Creates CNF that describes a single graph

    Args:
        G_edges (list): List of tuples, containing all (directed) edges in graph G

    Returns:
        list: CNF represented as list of clauses 
    """

    cnf = []
    for x in allVertices():
        for y in allVertices():
            if (x,y) in G_edges:
                cnf.append((posEdgeLiteral(x,y),))
            else:
                cnf.append((negEdgeLiteral(x,y),))
    return cnf

##################################
# Literal decoding
##################################

def get_edge_xy(edge_literal, v):
    """Decodes edge literal into origin and destination nodes

    Args:
        edge_literal (int): Edge literal
        v (int): Number of vertices

    Returns:
        tuple: edge origin x and destination y nodes as (x,y)
    """

    assert 1<=v<v**2
    return divmod(edge_literal, v)

@lru_cache(maxsize=None)
def get_graph(graph_int, v):
    """Decodes graph literal into interpretable form

    Args:
        graph_int (int): Graph literal
        v (int): Number of vertices

    Returns:
        list: List of edge tuples
    """

    assert graph_int < 2**(v**2)
    n_edges = v**2
    max_bin_rep = len(bin(n_edges)[2:])
    binary_repr = str(bin(graph_int))[2:]
    binary_repr = "0"*(max_bin_rep-len(binary_repr))+binary_repr
    edges = [get_edge_xy(i,v) for i, digit in enumerate(reversed(binary_repr)) if digit=="1"]
    return edges

def all_edge_tuples():
    """Gives all possible edges, whether they are real or not.

    Returns:

    """
    #a = list(permutations(allVertices(),2)) + [(i,i) for i in allVertices()]
    #a.sort()

    return [get_edge_xy(ed, config.v) for ed in allEdges()]