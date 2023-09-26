from collections import deque

rows, cols = [int(num) for num in input().split()]
matrix = [['x' for c in range(cols)] for r in range(rows)]
string = deque(input())
range_forwards = range(cols)
range_backwards = range(cols, 0, -1)


for row in range(rows):
    if row % 2 == 0:
        for col in range_forwards:
            matrix[row][col] = string[0]
            string.rotate(-1)
    else:
        for col in range_backwards:
            matrix[row][col-1] = string[0]
            string.rotate(-1)

print('\n'.join([''.join([x for x in el]) for el in matrix]))