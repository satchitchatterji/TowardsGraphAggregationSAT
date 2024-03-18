from itertools import permutations


def generate_profiles(n_agents=3,n_nodes=3):
    n_graphs=13
    asp = """"""
    
    perms = list(permutations(range(1,n_graphs+1),n_agents))
    for i in range(1,n_graphs+1):
        perms += list([i] * n_agents)