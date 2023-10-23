def find_t_positions(trace_):
    t1_position_ = None
    t2_position_ = None
    t_counter = 0
    for r in range(size):
        for c in range(size):
            if trace_[r][c] == 'T':
                t_counter += 1
                if t_counter == 1:
                    t1_position_ = [r, c]
                elif t_counter == 2:
                    t2_position_ = [r, c]
    return t1_position_, t2_position_


def move(position_, direction_):
    if direction_ == 'up':
        position_[0] -= 1
    elif direction_ == 'down':
        position_[0] += 1
    elif direction_ == 'left':
        position_[1] -= 1
    elif direction_ == 'right':
        position_[1] += 1
    return position_


size = int(input())
racing_number = input()
trace = [list(input().split()) for _ in range(size)]
position = [0, 0]
trace[position[0]][position[1]] = 'C'
STEP_DIRECTION = 10
total_kms = 0
t1_position, t2_position = find_t_positions(trace)

direction = input()
while direction != 'End':
    trace[position[0]][position[1]] = '.'  # marking old position with '.'
    position = move(position, direction)  # finding new position coordinates
    new_row, new_col = position

    if trace[new_row][new_col] == 'T':
        trace[t1_position[0]][t1_position[1]] = '.'
        trace[t2_position[0]][t2_position[1]] = '.'
        if t1_position == [new_row, new_col]:
            position = t2_position
        elif t2_position == [new_row, new_col]:
            position = t1_position
        trace[position[0]][position[1]] = 'C'
        total_kms += 30
    elif trace[new_row][new_col] == 'F':
        trace[new_row][new_col] = 'C'
        total_kms += STEP_DIRECTION
        print(f'Racing car {racing_number} finished the stage!')
        break
    else:
        total_kms += STEP_DIRECTION
        trace[new_row][new_col] = 'C'
    direction = input()
else:
    print(f'Racing car {racing_number} DNF.')
print(f'Distance covered {total_kms} km.')
print('\n'.join([''.join([el for el in x]) for x in trace]))
