n_rows = int(input())
matrix = [[int(col) for col in input().split()] for el in range(n_rows)]

# finding the diagonals
primary_diagonal = [matrix[index][index] for index in range(len(matrix))]
secondary_diagonal = [matrix[index][-index-1] for index in range(len(matrix))]

# finding the difference
diagonal_difference = abs(sum(primary_diagonal)-sum(secondary_diagonal))

print(diagonal_difference)