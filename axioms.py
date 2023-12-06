from config import config
from itertools import permutations
from utils import allVertices, allProfiles, allVoters, get_graph
from literals import *
from math import factorial

from functools import lru_cache


def get_all_profiles():
	return permutations(config.graphs, config.v)

def index_profile(tup):
	return list(get_all_profiles()).index(tup)

def anonymity():
	cnf = []
	exp_c = config.r*factorial(config.v)*config.v*config.v
	print("Expected clauses: ", exp_c)
	# return exp_c
	for profile1 in get_all_profiles(config.graph_list):
		perms = permutations(profile1)
		for profile2 in perms:
			p1, p2 = index_profile(profile1), index_profile(profile2)
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


def nondictatorship():
	cnf = []
	exp_c = config.r*config.n*config.n*config.e
	print("Expected clauses: ", exp_c)
	# return exp_c
	for profile in get_all_profiles():
		E = index_profile(profile)
		for i in allVoters():
			for graph_id in profile:
				graph = get_graph(graph_id, config.v)
				for (x,y) in graph:
					# (p or e) and (not p or not e)
					cnf.append((posEdgePlayerLiteral(E,x,y,i), posLiteral(E,x,y)))
					cnf.append((negEdgePlayerLiteral(E,x,y,i), negLiteral(E,x,y)))
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
