#  Nicholas AW Wright
#  April 2023

# source: https://www.geeksforgeeks.org/permutation-and-combination-in-python/#
# source: https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
# A Python program to print all permutations using library function
from itertools import permutations,product
import copy
import time
import multiprocessing

# Program Description
'''
This program uses brute force to attempt assembling Pavel's Puzzles' Octamaze octahedron.
It tests out every possible permutation of 8 pieces in each cartesian product possibility
of rotations to see if the pieces fit together. If they do fit, the solution is printed out
and the program continues to run. There is only a single unique assembly solution, but all
of the possibilities together result in 24 different views of this unique assembly. One can
visualize this outcome by spinning the octahedron around its vertical axis and realizing that
each of the four faces could come first in a permutation that satisfies the solution criteria.
There are 6 corners that could possibly point upwards, each with 4 solution satisfying
permutations, thus leading to a total of 24 solution satisfying arrays, which are all the 
same element of a set.
'''

# Representing the Puzzle Pieces
'''
Each of the puzzle piece sides has a small tab, a large tab, a small slot, or a large slot
Let each of these possible connectors be represented by the numbers 1,2,-1,-2, respectively
Then, for two connectors to mate as intended, their sum must be zero

We represent the three triangle sides as an array:
'''
# [x y z]
'''
Where x is the corner to the left, z is the corner to the right, and y is either pointing up or down

If we flip a piece 180deg, such that y goes from pointing up to pointing down, then x and z must swap
That is:

    (up)     (down)   '''
# [x y z] = [z y x]
'''
So, each of the triangluar puzzle pieces is represented by an list of integers from the set {-2,-1,1,2}
An example piece is:
'''
# p103 = [2, 1,-2]
'''
Where the sides corresponding to the written numbers have the connectors large tab, small tab, large slot,
respectively

We can also spin each of the pieces independently, such that each has 3 possible representations as follows:
'''
# position 0 = [x y z]
# position 1 = [z x y]
# position 2 = [y z x]
'''
We want to try each permutation of 8 pieces in every cartesian product of possible spin orientations
'''


# Solution Criteria
'''
Let each of the 8 triangular pieces by denoted as the set {A,B,C,...,H}
An "unwrapped" side view of the solution will look like
'''
#  A B C D
#  E F G H
'''
Where A,B,C,D are triangles pointing up and E,F,G,H are triangles pointing down.

For the configuration to be valid assembly solution, the sum of all adjacent connectors must be zero:
'''
#  A <--0--> B <--0--> C <--0--> D --0-->
#  ^         ^         ^         ^
#  |         |         |         |
#  0         0         0         0
#  |         |         |         |
#  v         v         v         v
#  E <--0--> F <--0--> G <--0--> H --0-->
'''
From the above diagram, it is clear that there are 12 sums that must be zero for a valid solution
This problem formulation requires rotating the bottom row by 180deg, so let us reformulate:
'''
# <--0-- A <--0--> B <--0--> C <--0--> D   |   E <--0--> F <--0--> G <--0--> H --0-->
#        ^         ^         ^         ^       ^         ^         ^         ^
#        |         |         |         |___0___|         |         |         |
#        |         |         |_____________0_____________|         |         |
#        |         |_______________________0_______________________|         |
#        |_________________________________0_________________________________|
'''
The above formulation maintains the 12 required sums, but avoids having to flip the bottom row
The letters now refer to different pieces than before, but that is okay as they are just variables
'''

# Tests for the solution criteria
def test_solution(pieces):
    A=pieces[0]
    B=pieces[1]
    C=pieces[2]
    D=pieces[3]
    E=pieces[4]
    F=pieces[5]
    G=pieces[6]
    H=pieces[7]
    
    if( A[0] + D[2] == 0 and
        A[1] + H[1] == 0 and
        A[2] + B[0] == 0 and
        B[1] + G[1] == 0 and
        B[2] + C[0] == 0 and
        C[1] + F[1] == 0 and
        C[2] + D[0] == 0 and
        D[1] + E[1] == 0 and
        E[2] + F[0] == 0 and
        F[2] + G[0] == 0 and
        G[2] + H[0] == 0 and
        H[2] + E[0] == 0    
        ):
        return pieces
    else: return 0


# Function for flipping pieces in place
# (Problem forumlation updated to avoid flipping)
def flip(pieces):
    for piece in pieces:
        first=piece[0]
        last=piece[2]
        piece[0]=last
        piece[2]=first
    return pieces


# Function to spin pieces in place
def spin(layout,orient):
    piece = 0
    for i in layout:
        for j in range(int(orient[piece])):
            layout[piece].append(layout[piece].pop(0))
        piece += 1
    return layout


def check_layout(layout):
    # Have to reset the iterator as it is consumed each loop: https://stackoverflow.com/a/3266353
    spinProduct = product('012',repeat=8)
    global iterCount
    global totalCount
    global solCount
    global t0
    global layoutCount
    with iterCount.get_lock():
            iterCount.value += 1
            if (iterCount.value%100 == 0):
                # print which iteration currently on for program execution status
                print(f"iteration = {iterCount.value}/{layoutCount} ({round(100*iterCount.value/layoutCount,2)}%)", end='\r')
    # print(iterCount.value)
    for orient in spinProduct:
        # # incrementing this variable each loop slows down execution considerably
        # with iterCount.get_lock():
        #     iterCount.value += 1
        #     if (iterCount.value%10000 == 0):
        #         # print which iteration currently on for program execution status
        #         print(f"iteration = {iterCount.value}/{totalCount} ({round(100*iterCount.value/totalCount,2)}%)", end='\r')
        # we must deep copy for each orientation, otherwise pieces will not be reset after spinning in place
        tempLayout = copy.deepcopy(layout)
        spin(tempLayout,orient)
        sol = test_solution(tempLayout)
        # print(iterCount)
        if sol: 
            with solCount.get_lock():
                solCount.value += 1
            print()
            print(f"Solution #{solCount.value} = {sol}")
            print(f"Time to solution #{solCount.value} = {round(time.time() - t0, 1)}s")
            print()
   

def defineLayouts(): 
    # Define Puzzle pieces
    p103 = [2, 1,-2]
    p271 = [2,-1,-2]
    p001 = [1, 1,-1]
    p250 = [1,-1, 2]
    p116 = [1,-2,-1]
    p130 = [2,-2, 2]
    p144 = [2,-2,-2]
    p063 = [1,-1,-1]

    pieces = [p103,p271,p001,p250,p116,p130,p144,p063]
 
    # Get all layout permutations of pieces
    '''We use a permutation because the pieces could be in any order'''
    piecePerms = permutations(pieces)
    # total number of piece layout permutations
    global layoutCount
    layoutCount = len(list(permutations(pieces)))
    print(f"Layout Permutations = {layoutCount}")

    # Get the cartesian product of possible spin orientations
    '''We use a cartesian product because each of the 8 pieces has 3 possible spin orientations'''
    spinProduct = product('012',repeat=8)
    # total number of cartesian product spin orientations
    spinProductCount = len(list(product('012',repeat=8)))
    print(f"spin Orientations = {spinProductCount}")

    # total number of possible configurations to check
    global totalCount
    totalCount = spinProductCount*layoutCount
    print(f"Total Configurations = {totalCount}")
    print()

    return piecePerms


def initMulti(arg1,arg2,arg3,arg4,arg5):
    ''' store the counter for later use '''
    global iterCount
    global totalCount
    global solCount
    global t0
    global layoutCount
    iterCount = arg1
    totalCount = arg2
    solCount = arg3
    t0 = arg4
    layoutCount = arg5

if __name__ == '__main__':
    # source: https://docs.python.org/3/library/multiprocessing.html
    # source: https://stackoverflow.com/questions/2080660/how-to-increment-a-shared-counter-from-multiple-processes
    global t0
    t0 = time.time()
    layouts = defineLayouts()
    iterCount = multiprocessing.Value('i', 0)
    solCount = multiprocessing.Value('i', 0)
    
    with multiprocessing.Pool(initializer = initMulti, initargs = (iterCount,totalCount,solCount,t0,layoutCount)) as allCores:
        allCores.map(check_layout, list(layouts))
    
    t1 = time.time()
    print(f"Total time for all iterations = {round(t1-t0,3)}s")
