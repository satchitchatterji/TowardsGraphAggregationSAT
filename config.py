# from math import factorial

# n = 2 # number of voters
# v = 3 # number of vertices
# g = 2**(v**2) # number of total directed graphs
# e = v**2 # number of possible directed edges

class config:
	n = 2 # number of voters
	v = 3 # number of vertices
	g = 2**(v**2) # number of total directed graphs
	e = v**2 # number of possible directed edges

	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_instance'):
			orig = super(config, cls)
			cls._instance = orig.__new__(cls, *args, **kw)
		return cls._instance

