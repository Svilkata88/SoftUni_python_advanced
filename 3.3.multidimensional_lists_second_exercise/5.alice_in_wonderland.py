n_size = int(input()) #  reading the size ot the matrix
wonderland_matrix = [[x for x in input().split()] for el in range(n_size)] #  reading the input for the matrix
alice_position = [0, 0]
for row in range(n_size):  # finding A position
    for col in range(n_size):
        if wonderland_matrix[row][col] == 'A':
            alice_position = [row, col]
tea_bags = 0
possible_commands = {'up':(-1,0), 'down':(1,0), 'left':(0,-1), 'right':(0,1)}

command = input()
wonderland_matrix[alice_position[0]][alice_position[1]] = '*'
while command:
    row, col = alice_position
    new_row = row + possible_commands[command][0]
    new_col = col + possible_commands[command][1]
    if new_row not in range(n_size) or new_col not in range(n_size):
        break
    if wonderland_matrix[new_row][new_col] == 'R':
        wonderland_matrix[new_row][new_col] = '*'
        break
    if wonderland_matrix[new_row][new_col].isdigit():
        tea_bags += int(wonderland_matrix[new_row][new_col])
    if tea_bags >= 10:
        wonderland_matrix[new_row][new_col] = '*'
        break
    wonderland_matrix[new_row][new_col] = '*'
    alice_position = [new_row, new_col]
    command = input()

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')
print('\n'.join([' '.join([x for x in el]) for el in wonderland_matrix]))