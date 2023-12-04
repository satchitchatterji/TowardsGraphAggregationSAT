from config import config
from itertools import permutations
from utils import allVertices, allProfiles, allVoters, get_graph
from literals import *

all_graphs = [1,2,3,4,5]
config.g = 5


def get_all_profiles(graphs):
	return permutations(graphs, config.v)

def index_profile(tup, graphs):
	return list(get_all_profiles(graphs)).index(tup)

def anonymity(graph_list):
	cnf = []
	for profile1 in get_all_profiles(graph_list):
		perms = permutations(profile1)
		for profile2 in perms:
			p1, p2 = index_profile(profile1, graph_list), index_profile(profile2, graph_list)
			for x in allVertices():
				for y in allVertices():
					cnf.append((negLiteral(p1, x, y), posLiteral(p2, x, y)))
	return cnf


def unanimity(graph_list):
	cnf = []
	for E in allProfiles():
		for x in allVertices():
			for y in allVertices():
				disj = []
				for i in allVoters():
					disj.append(negEdgePlayerLiteral(E,x,y,i))
				disj.append(posLiteral(E,x,y))
				cnf.append(tuple(disj))

	return cnf


def grounded(graph_list):
	cnf = []
	for E in allProfiles():
		for x in allVertices():
			for y in allVertices():
				for i in allVoters():
					cnf.append((negLiteral(E,x,y), posEdgePlayerLiteral(E,x,y,i)))
	return cnf


def nondictatorship(graph_list):
	cnf = []
	for profile in get_all_profiles(graph_list):
		E = index_profile(profile, graph_list)
		for i in allVoters():
			for graph_id in profile:
				graph = get_graph(graph_id, config.v)
				for (x,y) in graph:
					# (p or e) and (not p or not e)
					cnf.append((posEdgePlayerLiteral(E,x,y,i), posLiteral(E,x,y)))
					cnf.append((negEdgePlayerLiteral(E,x,y,i), negLiteral(E,x,y)))
	return cnf


def iie(graph_list):
	cnf = []
	for E1 in allProfiles():
		for E2 in allProfiles():
			for x in allVertices():
				for y in allVertices():
					cnf.append((negLiteral(E1,x,y), posLiteral(E2,x,y)))
					cnf.append((posLiteral(E1,x,y), negLiteral(E2,x,y)))
	return cnf
