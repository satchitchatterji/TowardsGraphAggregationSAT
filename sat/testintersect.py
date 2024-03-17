from literals import *
from utils import *
# from axioms import get_all_profiles, index_profile

def get_profile(profile_int):
    dims = [config.g]*config.n
    return tuple(calculate_coordinates(profile_int, dims))

if __name__ == '__main__':

    # graphs = [38, 44, 104, 134, 194, 200]
    graphs = [0,1,2,3,4,5]
    config.update_graphs(graphs)
    # print(vars(config))

    player = []
    winner = []
    for E in allProfiles():
        for x in allVertices():
            for y in allVertices():
                winner.append(posLiteral(E,x,y))
                for i in allVoters():
                    player.append(posEdgePlayerLiteral(E,x,y,i))

    intersect = [value for value in player if value in winner]
    print(intersect)
    allprofs = list(allProfiles())
    # print(len(allprofs))
    # print(config.r)
    lit = -123
    lit = (config.n)*config.r*config.v*config.v+4
    decoded = decodeLiteral(lit, LITDIM)
    # print("(i,E,x,y):", decoded)
    print("Literal:", lit)
    if len(decoded) == 4:
        print(f"\tplayer {decoded[0]}: profile {get_profile(allprofs[decoded[1]])} -> winning edge from {decoded[2]} to {decoded[3]}")
        print(f"\te_{decoded[1]},{decoded[2]},{decoded[3]},{decoded[0]}")
        print("\tre-encoded:", posEdgePlayerLiteral(decoded[1], decoded[2],decoded[3],decoded[0]))
    else:
        print(f"\tedge: profile {get_profile(allprofs[decoded[0]])} -> winning edge from {decoded[1]} to {decoded[2]}")
        print(f"\tp_{decoded[0]},{decoded[1]},{decoded[2]}")
        print("\tre-encoded:", posLiteral(decoded[0], decoded[1], decoded[2]))


