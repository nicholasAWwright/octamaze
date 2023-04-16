#  Nicholas AW Wright
#  April 2023

# source: https://www.geeksforgeeks.org/permutation-and-combination-in-python/#
# source: https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
# A Python program to print all permutations using library function
from itertools import permutations,product
import copy
import time


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

# Used for flipping pieces in place
def Reverse(pieces):
    for piece in pieces:
        first=piece[0]
        last=piece[2]
        piece[0]=last
        piece[2]=first
    return pieces

def TestSolution(pieces):
    solved=0
    A=pieces[0]
    B=pieces[1]
    C=pieces[2]
    D=pieces[3]
    E=pieces[4]
    F=pieces[5]
    G=pieces[6]
    H=pieces[7]
    
    if( A[0] + D[2] == 0 and
        A[1] + E[1] == 0 and
        A[2] + B[0] == 0 and
        B[1] + F[1] == 0 and
        B[2] + C[0] == 0 and
        C[1] + G[1] == 0 and
        C[2] + D[0] == 0 and
        D[1] + H[1] == 0 and
        E[0] + H[2] == 0 and
        E[2] + F[0] == 0 and
        F[2] + G[0] == 0 and
        G[2] + H[0] == 0    ):
        solved = 1
    if solved: return pieces
    else: return

def Spin(layout,orient):
    orientElem = 0
    layoutElem = 0
    for i in layout:
        # print(layoutElem,orientElem)
        # print()
        # print(range(int(orient[orientElem])))
        # print(f"before spin = {layout[layoutElem]}")
        # print(f"spin = {orient[orientElem]}")
        for j in range(int(orient[orientElem])):
            layout[layoutElem].append(layout[layoutElem].pop(0))
        # numpy.roll(layout[layoutElem],int(orient[orientElem]))
        # print(f"after spin = {layout[layoutElem]}")
        layoutElem += 1
        orientElem += 1
    return layout

 
# Puzzle pieces
p103 = [2, 1,-2]
p271 = [2,-1,-2]
p001 = [1, 1,-1]
p250 = [1,-1, 2]
p116 = [1,-2,-1]
p130 = [2,-2, 2]
p144 = [2,-2,-2]
p063 = [1,-1,-1]

pieces = [p103,p271,p001,p250,p116,p130,p144,p063]
upper4 = pieces[0:4]
lower4 = pieces[4:8]
# print(f"upper = {upper4}")
# print(f"lower = {lower4}")
# print(f"lower reversed = {reverse(lower4)}")
# print(f"lower = {lower4}")
 
# Get all layout permutations of pieces
piecePerms = permutations(pieces)
spinProduct = product('012',repeat=8)
piecePermsCount = len(list(permutations(pieces)))
spinProductCount = len(list(product('012',repeat=8)))
totalCount = spinProductCount*piecePermsCount
print(f"Spin Orientations = {spinProductCount}")
print(f"Layout Permutations = {piecePermsCount}")
print(f"Total Possibilities = {totalCount}")

# spinCount = 0
# for orient in spinProduct:
#     spinCount += 1
#     print(orient)
# print(f"Spin Orientations = {spinCount}")

# layoutCount = 0
# # Print the obtained permutations
# for layout in list(piecePerms):
#     layoutCount += 1
# print(f"permutations = {layoutCount}")

# print(f"total iterations = {layoutCount*spinCount}")

t0 = time.time()
iterCount = 0
solCount = 0
for layout in list(piecePerms):
    print(f"iteration = {iterCount}/{totalCount} ({round(100*iterCount/totalCount,2)}%)", end='\r')
    upper = copy.deepcopy(layout[0:4])
    lower = copy.deepcopy(layout[4:8]) 
    # print(f"layout before reverse = {layout}")
    Reverse(lower) # bottom 4 pieces are spun 180 for ease of visualization
    reversedLayout = (upper[0],upper[1],upper[2],upper[3],lower[0],lower[1],lower[2],lower[3])
    # print(f"layout after reverse = {layout}")
    # print(layout)
    # print(f"upper = {upper}")
    # print(f"lower = {lower}")

    spinProduct = product('012',repeat=8)
    for orient in spinProduct:
        iterCount += 1
        tempLayout = copy.deepcopy(reversedLayout)
        # print(f"layout     before spin = {reversedLayout}")
        # print(f"tempLayout before spin = {tempLayout}")
        # print()
        Spin(tempLayout,orient) # TODO: this should work on a copy of the object
        # print(f"layout     after spin = {reversedLayout}")
        # print(f"tempLayout after spin = {tempLayout}")
        # print()
        # print(f"spin = {orient}")
        # print(f"layout after spin = {layout}")
        sol = TestSolution(tempLayout)
        if sol: 
            solCount += 1
            print()
            print(f"Solution #{solCount} = {sol}")
            print(f"Time to solution #{solCount} = {round(time.time() - t0, 3)} seconds")
            # break
    else:
        # print(spinChecks)
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break
t1 = time.time()
print(f"Total time for all iterations = {round(t1-t0,3)}s")

# print(f"Stopped on iteration {iterCount} out of a total possible {totalCount}")
# TODO: compile and run this so that it is much faster
