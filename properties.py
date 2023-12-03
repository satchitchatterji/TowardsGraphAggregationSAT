from utils import (
    allVertices,
    allVoters,
    allGraphs,
    allEdges,
    posEdgeLiteral, # (node x, node y)
    negEdgeLiteral, # (node x, node y)
)

def cnfReflexivity(V):
    """Reflexivity property

    Returns:
        cnf: List of tuples containing clauses for reflexivity CNF
    """
    cnf = []

    # edge from x to x for each note
    for x in allVertices():
        cnf.append((posEdgeLiteral(x,x)))

    return cnf

def cnfIrreflexivity(V):
    """Irreflexivity property

    Returns:
        cnf: List of tuples containing clauses for irreflexivity CNF
    """
    cnf = []

    for x in allVertices():
        cnf.append((negEdgeLiteral(x,x)))

    return cnf

def cnfTransitivity(V):
    """Transitivity property

    Returns:
        cnf: List of tuples containing clauses for transitivity CNF
    """
    cnf = []

    for x in allVertices():
        for y in allVertices():
            for z in allVertices():
                cnf.append((negEdgeLiteral(x,y),
                            negEdgeLiteral(y,z),
                            posEdgeLiteral(x,z)))

    return cnf

def cnfCompleteness(V):
    """Completeness property

    Returns:
        cnf: List of tuples containing clauses for completeness CNF
    """
    cnf = []
    
    for x in allVertices():
        for y in allVertices():
            if x != y:
                cnf.append((posEdgeLiteral(x,y), posEdgeLiteral(y,x)))
    
    return cnf

def cnfConnectedness(V):
    """Reflexivity property

    Returns:
        cnf: List of tuples containing clauses for connectedness CNF
    """
    cnf = []

    for x in allVertices():
        for y in allVertices():
            for z in allVertices():
                cnf.append((negEdgeLiteral(x,y), negEdgeLiteral(x,z), posEdgeLiteral(y,z)))
                cnf.append((negEdgeLiteral(x,y), negEdgeLiteral(x,z), posEdgeLiteral(z,y)))

    return cnf

def cnfNontriviality(V):
    """Reflexivity property

    Returns:
        cnf: List of tuples containing clauses for nontriviality CNF
    """
    cnf = []

    clause = []
    for x in allVertices():
        for y in allVertices():
            clause.append(posEdgeLiteral(x,y))

    cnf.append(tuple(posEdgeLiteral))

    return cnf

def cnfSeriality(V):
    """Seriality property

    Returns:
        cnf: List of tuples containing clauses for seriality CNF
    """
    cnf = []

    for x in allVertices():
        clause = []
        for y in allVertices():
            clause.append(posEdgeLiteral(x,y))
        cnf.append(tuple(clause))
    return cnf