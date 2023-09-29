string = input().split('|')

matrix = []
for i in range(len(string)):
    row = string[i].split()
    if row:
        matrix.append(row)

matrix.reverse()
print(' '.join([' '.join([str(x) for x in el]) for el in matrix]))