from config import config
from literals import (
    posEdgeLiteral,
    negEdgeLiteral,
    calculate_index,
    calculate_coordinates
)

from pysat.solvers import Glucose3

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

def generate_graph_subsets(cnf_properties):
    def solve(cnf):
        solver = Glucose3()
        for clause in cnf: solver.add_clause(clause)
        if solver.solve():
            return solver.get_model()
        else:
            return('UNSATISFIABLE')

    acceptable_graphs = []
    for graph_int in allGraphs():
        edges = get_graph(graph_int, config.v)
        cnf = graphCNF(edges)
        for cnf_property in cnf_properties:
            cnf += cnf_property()
#         print(cnf)
        if solve(cnf) != 'UNSATISFIABLE':
            acceptable_graphs.append(graph_int)
            
    return acceptable_graphs

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

def profileIntToProfile(profile_int):
    """Decodes profile integer/index into a list of graph ints

    Args:
        profile_int (int): the profile int from [0, ..., config.r]

    Returns:
        tuple: list of graphs where each graph is from [0, ..., 2**(v**2)]
    """
    dims = [config.g]*config.n
    gr_indices = tuple(calculate_coordinates(profile_int, dims))
    grs = [config.graphs[x] for x in gr_indices]
    return tuple(grs)

def profileToProfileInt(profile):
    """Encodes a list of graph ints into profile integer/index

    Args:
        profile: list of graphs where each graph is from [0, ..., 2**(v**2)]

    Returns:
        int: the profile int from [0, ..., config.r]
    """
    gr_indices = [config.graphs.index(x) for x in profile]
    dims = [config.g]*config.n
    return calculate_index(gr_indices, dims)

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

# @lru_cache(maxsize=None)
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