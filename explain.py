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

from properties import (
    cnfReflexivity,
    cnfTransitivity,
    cnfCompleteness,
    cnfIrreflexivity,
    cnfNontriviality,
    cnfSeriality,
    cnfConnectedness
)

from literals import (
    posEdgeLiteral, # (node x, node y)
    negEdgeLiteral, # (node x, node y)
    LITDIM,
    EDGEDIM,
    PLAYERDIM,
    decodeLiteral
)

from axioms import (
	anonymity,
	unanimity,
	grounded,
	nondictatorship,
	iie,
    collectiverationality
)

from config import config

v = config.v
e = config.e
n = config.n
g = config.g



class Explain:



    def __init__(self, axiom_fns, prop_fns=None):
        all_fns = {"Anonymous": anonymity,
         "Unanimous": unanimity,
         "Grounded": grounded,
         "Nondictatorial": nondictatorship,
         "Independent": iie}


        self.axioms = {}
        for k,v in all_fns.items():
            #if v in axiom_fns and v == collectiverationality:
            #    self.axioms[k] = v(prop_fns)
            if v in axiom_fns:
                self.axioms[k] = v()
        
        if prop_fns is not None:
            self.add_props(prop_fns)


    def add_props(self, prop_fns):
        all_fns = {"Reflexive": cnfReflexivity,
                   "Complete": cnfCompleteness,
                   "Transitive": cnfTransitivity,
                   "Irreflexive": cnfIrreflexivity,
                   "Connected": cnfConnectedness,
                   "Nontrivial": cnfNontriviality,
                   "Serial": cnfSeriality}
        
        for k,v in all_fns.items():
            if v in prop_fns:
                self.axioms[k] = collectiverationality([v])
            

    def __call__(self, cnf: list):
        """Prints explanation for each clause in a given CNF

        Args:
            cnf (list): List of clauses
        """
        for clause in cnf: self.explainClause(clause)

    def strProf(self, E):
        graphs = profileIntToProfile(E)
        graph_edges =  [get_graph(graph_int, config.v) for graph_int in graphs]
        big_str = ",\n".join([str(ge) for ge in graph_edges])
        return big_str

    def strClause(self, clause):
        return ' or '.join(self.strLiteral(lit) for lit in clause)

    def strLiteral(self, lit):
        """Prints literal as an a->b implication

        Args:
            lit (_type_): _description_

        Returns:
            _type_: _description_
        """
        E,x,y = decodeLiteral(lit, LITDIM)
        #print(E,x,y)
        return ('not ' if lit<0 else '') + self.strProf(E) + f'\n-> ({x},{y})'

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


    print(ex([(156,), (65,), (99,), (33,)]))