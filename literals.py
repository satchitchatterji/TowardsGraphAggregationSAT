from config import *

def calculate_index(coordinates, dimensions):
    # unique index of a point with coordinates 'coordinates'
    # in a nD box of dimension n, with max size 'dimensions'
    idx = coordinates[0]
    for i in range(1, len(coordinates)):
        idx = idx * dimensions[i] + coordinates[i]
    return idx

def posEdgeLiteral(x, y):
    # used only for properties
    return calculate_index((x,y), (config.v, config.v)) + 1
    # return x*config.v+y+1

def negEdgeLiteral(x, y):
    # used only for properties
    return -posEdgeLiteral(x,y)

def posLiteral(E, x, y):
    return calculate_index((config.n, E,x,y), (config.n, config.r, config.v, config.v)) + 1

def negLiteral(E, x, y):
    return -posLiteral(E,x,y)

# def posEdgePlayerLiteral(E, x, y, i):
    # return (E+1) * (i*posEdgeLiteral(config.v-1,config.v-1) + posEdgeLiteral(x,y))

def posEdgePlayerLiteral(E, x, y, i):
    return calculate_index((E,x,y,i), (config.r, config.v, config.v, config.n)) + 1

    # return E*config.r+ i*config.n + x*config.v + y + 1

# E is profile
def negEdgePlayerLiteral(E, x, y, i):
    return -posEdgePlayerLiteral(E, x, y, i)
