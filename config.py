from math import factorial
from itertools import permutations
# n = 2 # number of voters
# v = 3 # number of vertices
# g = 2**(v**2) # number of total directed graphs
# e = v**2 # number of possible directed edges

def compute_r(g,v):
	return g**v
	
class config:
	n = 3 # number of voters
	v = 3 # number of vertices
	g = 2**(v**2) # number of total directed graphs
	e = v**2 # number of possible directed edges
	r = compute_r(g, v)

	graphs = list()

	def update_g(g, internal=False):
		print(f"Updating config.g := {g}")
		if g != len(config.graphs) and not internal:
			print(f"Warning: Requested update does not match internal state!")
			print(f"\tRequested update: g={g}, number of graphs saved: len(config.graphs=){len(config.graphs)}")
		config.g = g
		config.r = compute_r(g, config.v)

	def update_graphs(graphs):
		print("Updating config.graphs")
		config.graphs = graphs
		config.update_g(len(config.graphs), internal=True)

	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_instance'):
			orig = super(config, cls)
			cls._instance = orig.__new__(cls, *args, **kw)
		return cls._instance


if __name__ == '__main__':
	print(config.g)
	print(config.r)
	config.update_g(3)
	print(config.g)
	print(config.r)
	graphs = [1,2,3,4]
	config.update_graphs(graphs)