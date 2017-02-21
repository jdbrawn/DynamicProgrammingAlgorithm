"""
 File: KnightH.py
 Course: COMPSCI 320

 Name: John David Brawn
 UPI: jbra988
 ID: 881548616
 Email: jdbrawn@bu.edu
"""

import sys
from queue import *

#with open('KnightE.txt') as f:
#    lines = f.readlines()
lines = sys.stdin.readlines()

counter = 0
valid = 1
while valid == 1:
    r, c = lines[counter].split()
    counter += 1
    valid = 0

    #print("r = ", r)
    #print("c = ", c)

    d = [[0 for i in range(int(c))] for j in range(int(r))]
    w = [[0 for i in range(int(c))] for j in range(int(r))]
    w[0][0] = 1
    seen = [[0 for i in range(int(c))] for j in range(int(r))]
    q = Queue()
    q.put([0, 0])

    while not q.empty():
        i, j = q.get()

        if i == int(r)-1 and j == int(c)-1:
            print(d[i][j], w[i][j])
            valid = 1
            break

        for move in [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-1, 2), (-2, 1), (2, -1)]:
            ni = i + move[0]
            nj = j + move[1]

            if ni >= int(r) or nj >= int(c) or ni < 0 or nj < 0:
                continue

            if seen[ni][nj] == 1 and d[ni][nj] == d[i][j] + 1:
                w[ni][nj] += w[i][j]

            if seen[ni][nj] == 0:
                seen[ni][nj] = 1
                d[ni][nj] = d[i][j] + 1
                w[ni][nj] = w[i][j]
                q.put([ni, nj])
