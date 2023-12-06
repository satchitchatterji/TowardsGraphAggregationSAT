from config import *

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
    return calculate_index((config.n, E,x,y), (config.n, config.r, config.v, config.v)) + 1

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

def posEdgePlayerLiteral(E, x, y, i):
    """Calculates positive literal for an edge given the player and profile

    Args:
        E (int): Profile
        x (int): Origin node
        y (int): Destination node
        i (int): Player

    Returns:
        int: Positive literal for CNF
    """
    return calculate_index((E,x,y,i), (config.r, config.v, config.v, config.n)) + 1

# E is profile
def negEdgePlayerLiteral(E, x, y, i):
    """Calculates negative literal for an edge given the player and profile

    Args:
        E (int): Profile
        x (int): Origin node
        y (int): Destination node
        i (int): Player

    Returns:
        int: Negative literal for CNF
    """
    
    return -posEdgePlayerLiteral(E, x, y, i)
