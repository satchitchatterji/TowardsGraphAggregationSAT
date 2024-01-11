from utils import (
    allVertices,
    allVoters,
    allGraphs,
    allEdges,

)

from literals import (
    posEdgeLiteral, # (node x, node y)
    negEdgeLiteral, # (node x, node y)
)

def cnfReflexivity():
    """Reflexivity property

    Returns:
        cnf: List of tuples containing clauses for reflexivity CNF
    """
    cnf = []

    # edge from x to x for each note
    for x in allVertices():
        cnf.append((posEdgeLiteral(x,x),))

    return cnf

def cnfIrreflexivity():
    """Irreflexivity property

    Returns:
        cnf: List of tuples containing clauses for irreflexivity CNF
    """
    cnf = []

    for x in allVertices():
        cnf.append((negEdgeLiteral(x,x),))

    return cnf

def cnfTransitivity():
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

def cnfCompleteness():
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

def cnfConnectedness():
    """Connectedness property

    Returns:
        cnf: List of tuples containing clauses for connectedness CNF
    """

    cnf = []

    for x in allVertices():
        for y in allVertices():
            for z in allVertices():
                cnf.append((negEdgeLiteral(x,y), negEdgeLiteral(x,z), posEdgeLiteral(y,z), posEdgeLiteral(z,y)))
                # cnf.append((negEdgeLiteral(x,y), negEdgeLiteral(x,z), posEdgeLiteral(z,y)))

    return cnf

def cnfNontriviality():
    """Nontriviality property

    Returns:
        cnf: List of tuples containing clauses for nontriviality CNF
    """
    cnf = []

    clause = []
    for x in allVertices():
        for y in allVertices():
            clause.append((posEdgeLiteral(x,y)))

    cnf.append((posEdgeLiteral,))

    return cnf

def cnfSeriality():
    """Seriality property

    Returns:
        cnf: List of tuples containing clauses for seriality CNF
    """
    cnf = []

    for x in allVertices():
        clause = []
        for y in allVertices():
            clause.append(posEdgeLiteral(x,y))
        cnf.append((clause,))
    return cnf

def cnfSymmetry():
    # xy.(xEy → yEx)
    cnf = []

    for x in allVertices():
        for y in allVertices():
            cnf.append((negEdgeLiteral(x,y),
                        posEdgeLiteral(y,x)))

    return cnf
