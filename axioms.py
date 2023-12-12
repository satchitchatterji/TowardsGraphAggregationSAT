from config import config
from itertools import permutations
from utils import allVertices, allProfiles, allVoters, get_graph, all_edges
from literals import *
from math import factorial

from functools import lru_cache


# def getProfileGraphs():
# 	return permutations(config.graphs, config.v)

# def index_profile(tup):
# 	return list(getProfileGraphs()).index(tup)

def profileIntToProfile(profile_int):
    dims = [config.g]*config.n
    return tuple(calculate_coordinates(profile_int, dims))

def profileToProfileInt(profile):
    dims = [config.g]*config.n
    return calculate_index(profile, dims)

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
	exp_c = config.r*config.v*config.v
	print("Expected clauses: ", exp_c)
	# return exp_c
	for E in allProfiles():
		for x in allVertices():
			for y in allVertices():
				disj = []
				for i in allVoters():
					disj.append(negEdgePlayerLiteral(E,x,y,i))
				disj.append(posLiteral(E,x,y))
				cnf.append(tuple(disj))

	return cnf



def unanimity_imp():
	cnf = []

	for E in allProfiles():
		# for winning origin
		for xwin in allVertices():
			# for winning target
			for ywin in allVertices():
				graphs_in_E = profileIntToProfile(E)
				for graph_int in graphs_in_E:
					if (xwin,ywin) not in get_graph(graph_int, config.v):
						# cnf.append((posLiteral(E,xwin,ywin),))
					# else:
						cnf.append((negLiteral(E,xwin,ywin),))
					break

	return cnf

def grounded():
	cnf = []
	exp_c =  config.r*config.v*config.v*config.n
	print("Expected clauses: ", exp_c)
	# return exp_c
	for E in allProfiles():
		for x in allVertices():
			for y in allVertices():
				for i in allVoters():
					cnf.append((negLiteral(E,x,y), posEdgePlayerLiteral(E,x,y,i)))
	return cnf


def grounded_imp():
	cnf = []

	for E in allProfiles():
		# for winning origin
		for xwin in allVertices():
			# for winning target
			for ywin in allVertices():
				graphs_in_E = profileIntToProfile(E)
				edge_exists_in_any_player = False
				for graph_int in graphs_in_E:
					if (xwin,ywin) in get_graph(graph_int, config.v):
						edge_exists_in_any_player = True
						break

				if not edge_exists_in_any_player:
					cnf.append((negLiteral(E,xwin,ywin),))

	return cnf



def nondictatorship():
	cnf = []
	for E in allProfiles():
		# gets all the graph ints
		voter_graphs = profileIntToProfile(E)
		

		
		for gr in voter_graphs:
			clause = []
			gr_edges = get_graph(gr, config.v)
			for (x,y) in all_edges():
				if (x,y) in gr_edges: # case where the voter has that edge
					clause.append(negLiteral(E,x,y))
				else: # case where the voter does not have the edge
					clause.append(posLiteral(E,x,y))
			cnf.append(tuple(clause))

	return cnf

def iie():
	cnf = []
	exp_c = config.r*config.r*config.v*config.v*2
	print("Expected clauses: ", exp_c)
	# return exp_c
	for E1 in allProfiles():
		for E2 in allProfiles():
			for x in allVertices():
				for y in allVertices():
					cnf.append((negLiteral(E1,x,y), posLiteral(E2,x,y)))
					cnf.append((posLiteral(E1,x,y), negLiteral(E2,x,y)))
	return cnf
