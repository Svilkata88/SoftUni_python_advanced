n_rows = int(input())
matrix = [[int(col) for col in input().split(', ')] for el in range(n_rows)]

primary_diagonal = [matrix[index][index] for index in range(len(matrix))]
secondary_diagonal = [matrix[index][-index-1] for index in range(len(matrix))]

# print option 1
print('Primary diagonal: ', end='')
print(*primary_diagonal, sep= ', ', end='.')
print(f' Sum: {sum(primary_diagonal)}')
print('Secondary diagonal: ', end='')
print(*secondary_diagonal, sep= ', ', end='.')
print(f' Sum: {sum(secondary_diagonal)}')

# print option 2
# print("Primary diagonal: {', '.join([str(el) for el in primary_diagonal]}. Sum: {sum(primary_diagonal)})