# source: https://www.geeksforgeeks.org/permutation-and-combination-in-python/#
# source: https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
# A Python program to print all
# permutations using library function
from itertools import permutations,product
# from collections import deque
import copy
import time

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
solCount = 0
for layout in list(piecePerms):
    print(f"iteration = {solCount}/{totalCount} ({round(100*solCount/totalCount,2)}%)", end='\r')
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
        solCount += 1
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
            print()
            print(sol)
            # break
    else:
        # print(spinChecks)
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break
t1 = time.time()
print(f"Total time for all iterations = {round(t1-t0,3)}s")

# print(f"Stopped on iteration {solCount} out of a total possible {totalCount}")
# TODO: compile and run this so that it is much faster
