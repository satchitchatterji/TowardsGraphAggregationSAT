from math import factorial

# n = 2 # number of voters
# v = 3 # number of vertices
# g = 2**(v**2) # number of total directed graphs
# e = v**2 # number of possible directed edges
def compute_r(g):
	return factorial(g)
	
class config:
	n = 3 # number of voters
	v = 2 # number of vertices
	g = 2**(v**2) # number of total directed graphs
	e = v**2 # number of possible directed edges
	r = compute_r(g)

	def update_g(g):
		print(f"Updating g = {g}")
		config.g = g
		config.r = compute_r(g)

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