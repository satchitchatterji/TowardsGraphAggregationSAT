from typing import Any
from utils import (
    allVertices,
    allVoters,
    allGraphs,
    allEdges,
    get_edge_xy,
    get_graph,
    profileIntToProfile,
    profileToProfileInt
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
	iie,
)

from config import config

v = config.v
e = config.e
n = config.n
g = config.g



class Explain:



    def __init__(self, axiom_fns):
        all_fns = {"Anonymous": anonymity,
         "Unanymous": unanimity,
         "Grounded": grounded,
         "Nondictatorial": nondictatorship,
         "Independent": iie}


        self.axioms = {}
        for k,v in all_fns.items():
            if v in axiom_fns:
                self.axioms[k] = v()

        """self.axioms = {
            "Anonymous": anonymity() if anonymity in axiom_fns else None,
            "Unanymous": unanimity() if unanimity in axiom_fns else None,
            "Grounded": grounded() if grounded in axiom_fns else None,
            "Nondictatorial": nondictatorship() if nondictatorship in axiom_fns else None,
            "Independent": iie() if iie in axiom_fns else None
        }"""

    def __call__(self, cnf: list):
        """Prints explanation for each clause in a given CNF

        Args:
            cnf (list): List of clauses
        """
        for clause in cnf: self.explainClause(clause)

    def strProf(self, E):
        return '(' + ','.join(g for g in E) + ')'

    def strClause(self, clause):
        return ' or '.join(self.strLiteral(lit) for lit in clause)

    def strLiteral(self, lit):
        """Prints literal as an a->b implication

        Args:
            lit (_type_): _description_

        Returns:
            _type_: _description_
        """
        E,x,y = profileIntToProfile(lit)
        print(E,x,y)
        return ('not ' if lit<0 else '') + self.strProf(E) + f'-> ({x},{y})'

    def explainClause(self, clause):
        """Prints interpretable explanation of CNF clause.

        Args:
            clause (tuple): tuple of positive/negative literals representing player graph edges
        """
        reason = next((k for k in self.axioms if clause in self.axioms[k]), 'None')
        print(reason + ': ' + self.strClause(clause))
        

if __name__ == "__main__":

    from pysat.solvers import Glucose3
    from utils import generate_graph_subsets
    from properties import *
    from axioms import *

    def solve(cnf):
        solver = Glucose3()
        for clause in cnf: solver.add_clause(clause)
        if solver.solve():
            return solver.get_model()
        else:
            return('UNSATISFIABLE')
    
    graphs = generate_graph_subsets([cnfIrreflexivity, cnfTransitivity, cnfCompleteness])
    # graphs = generate_graph_subsets([cnfIrreflexivity, cnfConnectedness, cnfTransitivity, cnfCompleteness])
    config.update_graphs(graphs)
    arrow_axioms = [iie, nondictatorship, unanimity, grounded]
    ex = Explain(arrow_axioms)
    print(ex([(-1,),(-2,),(3,)]))