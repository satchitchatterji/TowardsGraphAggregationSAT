from config import *

def posEdgeLiteral(x, y):
    return x*v+y+1

def negEdgeLiteral(x, y):
    return -posEdgeLiteral(x,y)