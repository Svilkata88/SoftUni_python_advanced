rows, cols = [int(num) for num in input().split()]
matrix = [input().split() for r in range(rows)]


while True:
    command = input()
    if command == 'END':
        break
    keyword, coordinates = command.split()[0], command.split()[1:]
    if keyword != 'swap' or len(coordinates) != 4:
        print('Invalid input!')
        continue
    first_pair_coordinates = [int(coordinates[0]), int(coordinates[1])]
    second_pair_coordinates = [int(coordinates[2]), int(coordinates[3])]
    if first_pair_coordinates[0] not in range(rows) \
        or first_pair_coordinates[1] not in range(cols) \
        or second_pair_coordinates[0] not in range(rows) \
        or second_pair_coordinates[1] not in range(cols):
        print('Invalid input!')
        continue

    matrix[first_pair_coordinates[0]][first_pair_coordinates[1]], \
        matrix[second_pair_coordinates[0]][second_pair_coordinates[1]] = \
        matrix[second_pair_coordinates[0]][second_pair_coordinates[1]], \
        matrix[first_pair_coordinates[0]][first_pair_coordinates[1]]
    print(' \n'.join([' '.join([str(element) for element in el]) for el in matrix]))




