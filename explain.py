from typing import Any
from utils import (
    allVertices,
    allVoters,
    allGraphs,
    allEdges,
    get_edge_xy,
    get_graph
)

from literals import (
    posEdgeLiteral, # (node x, node y)
    negEdgeLiteral, # (node x, node y)
)

from axioms import (
	anonymity,
	unanimity,
	grounded,
	nondictatorship,
	iie
)

from config import config

v = config.v
e = config.e
n = config.n
g = config.g



class Explain:



    def __init__(self, axiom_fns):
        self.axioms = {
            "Anonymous": anonymity() if anonymity in axiom_fns else None,
            "Unanymous": unanimity() if unanimity in axiom_fns else None,
            "Grounded": grounded() if grounded in axiom_fns else None,
            "Nondictatorial": nondictatorship() if nondictatorship in axiom_fns else None,
            "Independent": iie() if iie in axiom_fns else None
        }


    def __call__(self, cnf: list):
        for clause in cnf: self.explainClause(clause)

    def strProf(self, r):
        return '(' + ','.join(self.strPref(i,r) for i in allVoters()) + ')'

    def strPref(self, i, r):
        return ''.join(str(x) for x in self.preflist(i,r))

    def strClause(self, clause):
        return ' or '.join(self.strLiteral(lit) for lit in clause)

    def strLiteral(self, lit):
        r = (abs(lit) - 1) // v
        x = (abs(lit) - 1) % e
        return ('not ' if lit<0 else '') + self.strProf(r) + '->' + str(x)

    def explainClause(self, clause):
        reason = next((k for k in self.axiom if clause in self.axiom[k]), 'None')
        print(reason + ': ' + self.strClause(clause))
        