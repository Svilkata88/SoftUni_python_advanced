rows, cols = [int(num) for num in input().split()]
matrix = [input().split() for r in range(rows)]
equal_el_squares = 0

for i_r in range(rows):
    if i_r + 1 not in range(rows):
        break
    for i_c in range(cols):
        if i_c + 1 in range(cols):
            up_left_element = matrix[i_r][i_c]
            up_right_element = matrix[i_r][i_c + 1]
            down_left_element = matrix[i_r + 1][i_c]
            down_right_element = matrix[i_r + 1][i_c + 1]
            if up_left_element == up_right_element == down_right_element == down_left_element:
                equal_el_squares += 1

        else:
            break

print(equal_el_squares)