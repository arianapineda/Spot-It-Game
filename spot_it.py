"""
Code to implement the game of Spot it!
"""

import comp140_module2 as spotit

def equivalent(point1, point2, mod):
    """
    Determines if the two given points are equivalent in the projective
    geometric space in the finite field with the given modulus.

    Each input point, point1 and point2, must be valid within the
    finite field with the given modulus.

    inputs:
        - point1: a tuple of 3 integers representing the first point
        - point2: a tuple of 3 integers representing the second point
        - mod: an integer representing the modulus

    returns: a boolean indicating whether or not the points are equivalent
    """
    point1_x = point1[0]
    point1_y = point1[1]
    point1_z = point1[2]
    point2_x = point2[0]
    point2_y = point2[1]
    point2_z = point2[2]
    new_x = ((point1_y*point2_z)-(point1_z*point2_y))%mod
    new_y = ((point1_z*point2_x)-(point1_x*point2_z))%mod
    new_z = ((point1_x*point2_y)-(point1_y*point2_x))%mod

    if (new_x == 0 and new_y == 0 and new_z == 0):
        return True
    return False

def incident(point, line, mod):
    """
    Determines if a point lies on a line in the projective
    geometric space in the finite field with the given modulus.

    The inputs point and line must be valid within the finite field
    with the given modulus.

    inputs:
        - point: a tuple of 3 integers representing a point
        - line: a tuple of 3 integers representing a line
        - mod: an integer representing the modulus

    returns: a boolean indicating whether or not the point lies on the line
    """
    point_x = point[0]
    point_y = point[1]
    point_z = point[2]
    line_a = line[0]
    line_b = line[1]
    line_c = line[2]
    sum_coord = line_a*point_x + line_b*point_y + line_c*point_z
    return (sum_coord%mod)==0
   

def generate_all_points(mod):
    """
    Generate all unique points in the projective geometric space in
    the finite field with the given modulus.

    inputs:
        - mod: an integer representing the modulus

    Returns: a list of unique points, each is a tuple of 3 elements
    """
    point_list = []
    for i_val in range(mod):
        for k_val in range(mod):
            for j_val in range(mod):
                point_list.append((i_val,k_val,j_val))
               
    point_list.pop(0)
    
    
    remove_points = []
    for point1 in point_list:
        for point2 in point_list[point_list.index(point1)+1: ]:
            if(equivalent(point1,point2, mod) and point2 not in remove_points):
                remove_points.append(point2)
    for point in remove_points:
        point_list.remove(point)    
    return point_list



def create_cards(points, lines, mod):
    """
    Create a list of unique cards.

    Each point and line within the inputs, points and lines, must be
    valid within the finite field with the given modulus.

    inputs:
        - points: a list of unique points, each represented as a tuple of 3 integers
        - lines: a list of unique lines, each represented as a tuple of 3 integers
        - mod: an integer representing the modulus

    returns: a list of lists of integers, where each nested list represents a card.
    """
    final_cards = []
    for line in lines:
        card = []
        for point in points:
            if incident(point,line,mod):
                card.append(points.index(point))
               
        final_cards.append(card)
    return final_cards

def run():
    """
    Create the deck and play the game.
    """
    # Prime modulus
    # Set to 2 or 3 during development
    # Set to 7 for the actual game
    modulus = 7

    # Generate all unique points for the given modulus
    points = generate_all_points(modulus)

    # Lines are the same as points, so make a copy
    lines = points[:]

    # Generate a deck of cards given the points and lines
    deck = create_cards(points, lines, modulus)

    # Run GUI - uncomment the line below after you have implemented
    #           everything and you can play your game.  The GUI does
    #           not work if the modulus is larger than 7.

    spotit.start(deck)

# Uncomment the following line to run your game (once you have
# implemented the run function.)

run()