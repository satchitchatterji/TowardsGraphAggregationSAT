from config import *
from math import factorial


def calculate_index(coordinates, dimensions):
    idx = coordinates[0]
    for i in range(1, len(coordinates)):
        idx = idx * dimensions[i] + coordinates[i]
    return idx

def get_total_profiles():
    return factorial(config.g)


def posEdgeLiteral(x, y):
    # used only for properties
    return calculate_index((x,y), (config.v, config.v)) + 1
    # return x*config.v+y+1

def negEdgeLiteral(x, y):
    # used only for properties
    return -posEdgeLiteral(x,y)


def posLiteral(E, x, y):
    return calculate_index((config.n, E,x,y), (config.n, get_total_profiles(), config.v, config.v)) + 1

def negLiteral(E, x, y):
    return -posLiteral(E,x,y)

# def posEdgePlayerLiteral(E, x, y, i):
    # return (E+1) * (i*posEdgeLiteral(config.v-1,config.v-1) + posEdgeLiteral(x,y))

def posEdgePlayerLiteral(E, x, y, i):
    return calculate_index((E,x,y,i), (get_total_profiles(), config.v, config.v, config.n)) + 1

    # return E*get_total_profiles()+ i*config.n + x*config.v + y + 1

# E is profile
def negEdgePlayerLiteral(E, x, y, i):
    return -posEdgePlayerLiteral(E, x, y, i)
