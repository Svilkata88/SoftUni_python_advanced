player_1, player_2 = input().split(', ')
maze = [list(input().split()) for el in range(6)]
turn = 1
active_player = None
loser = None
resting = {player_1: False, player_2: False}

coordinates = (int(el) for el in input().strip('()').split(", "))
while coordinates:
    active_player = player_1 if turn % 2 != 0 else player_2
    loser = "Tom" if active_player == "Jerry" else "Jerry"
    if resting[active_player]:
        resting[active_player] = False
        turn += 1
        coordinates = (int(el) for el in input().strip('()').split(", "))
        continue

    pos_1, pos_2 = coordinates
    if maze[pos_1][pos_2] == 'E':
        print(f'{active_player} found the Exit and wins the game!')
        break
    elif maze[pos_1][pos_2] == 'T':
        turn -= 1
        print(f'{active_player} is out of the game! The winner is {loser}.')
        break
    elif maze[pos_1][pos_2] == 'W':
        resting[active_player] = True
        print(f'{active_player} hits a wall and needs to rest.')
    else:
        pass
    turn += 1
    coordinates = (int(el) for el in input().strip('()').split(", "))
print(*maze, sep='\n')