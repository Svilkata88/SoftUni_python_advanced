def search_the_matrix(nice_kids, santa_position):
    for r in range(n_size):
        for c in range(n_size):
            if neighborhood_matrix[r][c] == 'V':
                nice_kids += 1
            elif neighborhood_matrix[r][c] == 'S':
                santa_position = [r, c]
    return nice_kids, santa_position


n_presents = int(input())
n_size = int(input())
neighborhood_matrix = [[x for x in input().split()] for el in range(n_size)]
directions = {'right': [0, 1], 'left': [0, -1], 'up': [-1, 0], 'down': [1, 0]}
nice_kids = 0
santa_position = [0, 0]
nice_kids, santa_position = search_the_matrix(nice_kids, santa_position)  # reads n nice kids and Santa position!
happy_nice_kids = 0

while n_presents > 0 and nice_kids > 0:
    command = input()
    if command == 'Christmas morning':
        break

    row, col = santa_position
    new_row = directions[command][0] + row
    new_col = directions[command][1] + col
    if new_row not in range(n_size) or col not in range(n_size):
        continue
    if neighborhood_matrix[new_row][new_col] == 'X':
        santa_position = [new_row, new_col]
        neighborhood_matrix[row][col] = '-'
        neighborhood_matrix[new_row][new_col] = 'S'
        continue
    elif neighborhood_matrix[new_row][new_col] == 'V':
        n_presents -= 1
        happy_nice_kids += 1
        nice_kids -= 1
        neighborhood_matrix[row][col] = '-'
        neighborhood_matrix[new_row][new_col] = 'S'
        santa_position = [new_row, new_col]
    elif neighborhood_matrix[new_row][new_col] == 'C':
        neighborhood_matrix[row][col] = '-'
        neighborhood_matrix[new_row][new_col] = 'S'
        if neighborhood_matrix[new_row - 1][new_col] == 'V':
            n_presents -= 1
            nice_kids -= 1
            happy_nice_kids += 1
            neighborhood_matrix[new_row - 1][new_col] = '-'
        elif neighborhood_matrix[new_row - 1][new_col] == 'X':
            n_presents -= 1
            neighborhood_matrix[new_row - 1][new_col] = '-'
        if neighborhood_matrix[new_row + 1][new_col] == 'V':
            n_presents -= 1
            nice_kids -= 1
            happy_nice_kids += 1
            neighborhood_matrix[new_row + 1][new_col] = '-'
        elif neighborhood_matrix[new_row + 1][new_col] == 'X':
            n_presents -= 1
            neighborhood_matrix[new_row + 1][new_col] = '-'
        if neighborhood_matrix[new_row][new_col - 1] == 'V':
            n_presents -= 1
            nice_kids -= 1
            happy_nice_kids += 1
            neighborhood_matrix[new_row][new_col - 1] = '-'
        elif neighborhood_matrix[new_row][new_col - 1] == 'X':
            n_presents -= 1
            neighborhood_matrix[new_row][new_col - 1] = '-'
        if neighborhood_matrix[new_row][new_col + 1] == 'V':
            n_presents -= 1
            nice_kids -= 1
            happy_nice_kids += 1
            neighborhood_matrix[new_row][new_col + 1] = '-'
        elif neighborhood_matrix[new_row][new_col + 1] == 'X':
            n_presents -= 1
            neighborhood_matrix[new_row][new_col + 1] = '-'
        santa_position = [new_row, new_col]
    else:
        neighborhood_matrix[row][col] = '-'
        neighborhood_matrix[new_row][new_col] = 'S'
        santa_position = [new_row, new_col]
        continue

if n_presents == 0 and nice_kids > 0:
    print('Santa ran out of presents!')
print('\n'.join([' '.join([x for x in el]) for el in neighborhood_matrix]))
if nice_kids == 0:
    print(f'Good job, Santa! {happy_nice_kids} happy nice kid/s.')
elif nice_kids > 0:
    print(f'No presents for {nice_kids} nice kid/s.')