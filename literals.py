from config import *

# define dimensions for outside use
LITDIM = (config.r, config.v, config.v)
PLAYERDIM = (config.n+1, config.r, config.v, config.v)
EDGEDIM = (config.v, config.v)

def calculate_index(coordinates, dimensions):
    """Calculates integer literal used to encode a specific edge, based on current CNF level.

    Args:
        coordinates (tuple): Tuple containing coords of specific index of vertex we want to describe
        dimensions (tuple): Tuple that indicates the dimensions fo the level "level of description" (e.g. player, profile, all profiles)

    Returns:
        int: Literal that encodes the relevant edge
    """
    # unique index of a point with coordinates 'coordinates'
    # in a nD box of dimension n, with max size 'dimensions'
    idx = coordinates[0]
    for i in range(1, len(coordinates)):
        idx = idx * dimensions[i] + coordinates[i]
    return idx

def calculate_coordinates(idx, dimensions):
    coordinates = [0] * len(dimensions)

    for i in range(len(dimensions) - 1, 0, -1):
        coordinates[i] = idx % dimensions[i]
        idx //= dimensions[i]

    coordinates[0] = idx
    return coordinates

def toEdgeLiteral(lit, dim=LITDIM):
    """Translates a literal of E,x,y or E,x,y,i encoding into a 
       player-independent, profile-independent, graph-specific x,y representation.

    Args:
        lit (int): Literal to convert
        dim (tuple, optional): Literal encoding dimensions. Defaults to LITDIM.
    """

    coords = decodeLiteral(lit,dim)
    x,y = coords[1], coords[2]

    return posEdgeLiteral(x,y) if lit > 0 else negEdgeLiteral(x,y), coords

def toLiteral(lit, E, dim=EDGEDIM):
    
    coords = decodeLiteral(lit,dim) 
    x,y = coords[0], coords[1]

    return posLiteral(E,x,y) if lit > 0 else negLiteral(E,x,y), coords

def decodeLiteral(lit, dim=PLAYERDIM):
    """Decodes info from a given player literal.

    Args:
        lit (int): Literal representing edge from x to y for player i in graph E.

    Returns:
        tuple: (E,x,y,i)
    """
    lit = abs(lit) - 1
  
    coords = calculate_coordinates(lit, dim)

    mult = dim[0]
    for d in dim[1:]:
        mult *= d

    if lit > config.r*config.v*config.v:
        return coords[1:]

    return coords

def posEdgeLiteral(x, y):
    """Encodes edge from node x to y as an integer. Used only for properties

    Args:
        x (int): Origin node
        y (int): Destination node

    Returns:
        int: Literal for CNF
    """
    # used only for properties
    return calculate_index((x,y), (config.v, config.v)) + 1
    # return x*config.v+y+1

def negEdgeLiteral(x, y):
    """Encodes negative edge from node x to y as an integer. Used only for properties

    Args:
        x (int): Origin node
        y (int): Destination node

    Returns:
        int: Literal for CNF
    """
    return -posEdgeLiteral(x,y)

def posLiteral(E, x, y):
    """Calculates positive literal for an edge given the profile

    Args:
        E (int): Profile
        x (int): Origin node
        y (int): Destination node

    Returns:
        int: Positive literal for CNF
    """
    return calculate_index((E,x,y), (config.r, config.v, config.v)) + 1
    #return posEdgePlayerLiteral(E, x, y, config.n)

def negLiteral(E, x, y):
    """Calculates negative literal for an edge given the profile

    Args:
        E (int): Profile
        x (int): Origin node
        y (int): Destination node

    Returns:
        int: Negative literal for CNF
    """
    return -posLiteral(E,x,y)


"""def posEdgePlayerLiteral(E, x, y, i):
    \"""Calculates positive literal for an edge given the player and profile

    Args:
        E (int): Profile
        x (int): Origin node
        y (int): Destination node
        i (int): Player

    Returns:
        int: Positive literal for CNF
    \"""
    return calculate_index((i,E,x,y), (config.n+1, config.r, config.v, config.v)) + 1

# E is profile
def negEdgePlayerLiteral(E, x, y, i):
    \"""Calculates negative literal for an edge given the player and profile

    Args:
        E (int): Profile
        x (int): Origin node
        y (int): Destination node
        i (int): Player

    Returns:
        int: Negative literal for CNF
    \"""
    
    return -posEdgePlayerLiteral(E, x, y, i)"""
