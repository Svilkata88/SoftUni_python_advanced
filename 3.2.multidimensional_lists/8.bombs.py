def detonation(row, col):
    if row in range(n_sides) and col in range(n_sides):
        cell_exploded = matrix[row][col]
        matrix[row-1][col-1] -= cell_exploded if matrix[row-1][col-1] > 0 else 0
        matrix[row-1][col] -= cell_exploded if matrix[row-1][col] > 0 else 0
        matrix[row-1][col+1] -= cell_exploded if matrix[row-1][col+1] > 0 else 0
        matrix[row][col-1] -= cell_exploded if matrix[row][col-1] > 0 else 0
        matrix[row][col+1] -= cell_exploded if matrix[row][col+1] > 0 else 0
        matrix[row+1][col-1] -= cell_exploded if matrix[row+1][col-1] > 0 else 0
        matrix[row+1][col] -= cell_exploded if matrix[row+1][col] > 0 else 0
        matrix[row+1][col+1] -= cell_exploded if matrix[row+1][col+1] > 0 else 0
        matrix[row][col] = 0
    return matrix

n_sides = int(input())
matrix = [[int(el) for el in input().split()] for r in range(n_sides)]
bombs = input().split()

for bomb in bombs:
    row, col = [int(el) for el in bomb.split(',')]
    detonation(row, col)
    break


print(*matrix, sep='\n')
print(*bombs)