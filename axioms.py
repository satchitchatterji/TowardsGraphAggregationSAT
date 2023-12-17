from config import config
from itertools import permutations
from utils import allVertices, allProfiles, allVoters, get_graph, all_edge_tuples, profileIntToProfile, profileToProfileInt
from literals import *
from math import factorial

from functools import lru_cache


# def getProfileGraphs():
# 	return permutations(config.graphs, config.v)

# def index_profile(tup):
# 	return list(getProfileGraphs()).index(tup)

def anonymity():
	cnf = []
	exp_c = config.r*factorial(config.v)*config.v*config.v
	print("Expected clauses: ", exp_c)
	# return exp_c
	for profile1 in allProfiles():
		perms = permutations(profileIntToProfile(profile1))
		print(perms)
		for profile2 in perms:
			p1, p2 = profileToProfileInt(profile1), profileToProfileInt(profile2)
			for x in allVertices():
				for y in allVertices():
					cnf.append((negLiteral(p1, x, y), posLiteral(p2, x, y)))
	return cnf

def unanimity():
	cnf = []

	for E in allProfiles():
		
		# flattens all voter graphs into one list
		graphs_in_E = [config.graphs[x] for x in profileIntToProfile(E)]
		all_edges = []
		for g in graphs_in_E:
			all_edges += get_graph(g, config.v)
		
		# counts occurrences of each graph
		edgecount = {}
		for edge in all_edges:
			if edge not in edgecount:
				edgecount[edge] = 0
			edgecount[edge] += 1

		# applies constraint to all relevant E,x,y
		for edge, count in edgecount.items():
			if count == config.n:
				x,y = edge
				cnf.append((posLiteral(E,x,y),))

	return cnf


def grounded():
	#add constraint that if no player has some edge (x,y), then it must not be in the winning graph.
	cnf = []

	for E in allProfiles():
		# for winning origin
		for xwin in allVertices():
			# for winning target
			for ywin in allVertices():
				graphs_in_E = profileIntToProfile(E)
				edge_exists_in_any_player = False
				for gr_int in graphs_in_E:
					graph_int = config.graphs[gr_int]
					if (xwin,ywin) in get_graph(graph_int, config.v):
						# matching edge found for this profile - no constraint required
						edge_exists_in_any_player = True
						break

				if not edge_exists_in_any_player:
					# matching edge not found for this profile - do not allow this E,x,y
					cnf.append((negLiteral(E,xwin,ywin),))

	return cnf



def nondictatorship():
	cnf = []

	# we enforce that each voter must have at least one situation where their graph is _not_ the winning graph.
	for i in allVoters():
		clause = []

		for E in allProfiles():
			voter_graphs = profileIntToProfile(E)
			gr_int = voter_graphs[i]
			gr_int = config.graphs[gr_int]
			gr_edges = get_graph(gr_int, config.v)
			for x,y in all_edge_tuples():
				if (x,y) in gr_edges: # case where the voter has that edge
					clause.append(negLiteral(E,x,y))
				else: # case where the voter does not have the edge
					clause.append(posLiteral(E,x,y))
			
		cnf.append(tuple(clause))

	return cnf

def iie():
	cnf = []
	exp_c = config.r*config.r*config.v*config.v*2
	print("Expected IIE clauses: ", exp_c)
	# return exp_c
	for E1 in allProfiles():
		
		graphs_in_E1 = [config.graphs[x] for x in profileIntToProfile(E1)]
		e1_edges = []
		for g in graphs_in_E1:
			e1_edges += get_graph(g, config.v)

		for E2 in allProfiles():
			#if E1 == E2:
			#	continue

			graphs_in_E2 = [config.graphs[x] for x in profileIntToProfile(E2)]
			e2_edges = []
			for g in graphs_in_E2:
				e2_edges += get_graph(g, config.v)
		
			for x in allVertices():
				for y in allVertices():
					if e1_edges.count((x,y)) == e2_edges.count((x,y)):
						# count the number of voters, if unequal then go next
						cnf.append((negLiteral(E1,x,y), posLiteral(E2,x,y)))
						cnf.append((negLiteral(E2,x,y), posLiteral(E1,x,y)))
	return cnf


def collectiverationality(prop_fns):
	"""Collective rationality wrapper fn. Enforces collective rationality
	   wrt given properties on winners of all existing profiles. 

    Args:
        props_fns (_type_): _description_
    """

	prop_cnf = []
	for fn in prop_fns:
		prop_cnf += fn()

	cnf = [] # properties, repeated for each profile
	# generate prof-prop clauses
	for E in allProfiles():
		for clause in prop_cnf:
			cnf.append(tuple([toLiteral(lit, E)[0] for lit in clause]))

	return cnf

def cr_fn(prop_fns):
	def cr(): return collectiverationality(prop_fns)
	return cr


if __name__=="__main__":
	from properties import cnfCompleteness, cnfTransitivity, cnfReflexivity
	from utils import generate_graph_subsets
	
	prop_fns = [cnfReflexivity, cnfTransitivity, cnfCompleteness]
	graphs = generate_graph_subsets(prop_fns)
	from config import config
	config.update_graphs(graphs)

	# def cr(): return collectiverationality(prop_fns)
	
	# print(len(list(cr())))
	print(len(unanimity()))