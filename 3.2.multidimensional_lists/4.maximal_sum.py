import math

rows, cols = [int(num) for num in input().split()]
matrix = [input().split() for r in range(rows)]
max_sum = -math.inf
max_sum_list = []

for i_r in range(rows):
    if i_r + 2 not in range(rows):
        break
    for i_c in range(cols):
        if i_c + 2 in range(cols):
            up_left_element = matrix[i_r][i_c]
            up_middle_element = matrix[i_r][i_c + 1]
            up_right_element = matrix[i_r][i_c + 2]

            middle_left_element = matrix[i_r + 1][i_c]
            middle_middle_element = matrix[i_r + 1][i_c + 1]
            middle_right_element = matrix[i_r + 1][i_c + 2]

            down_left_element = matrix[i_r + 2][i_c]
            down_middle_element = matrix[i_r + 2][i_c + 1]
            down_right_element = matrix[i_r + 2][i_c + 2]

            current_sum_list = [
                [up_left_element, up_middle_element, up_right_element],
                [middle_left_element, middle_middle_element, middle_right_element],
                [down_left_element, down_middle_element, down_right_element]
            ]

            current_sum = [[int(el) for el in num] for num in current_sum_list]
            current_sum = sum(sum(el) for el in current_sum)
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_list = current_sum_list

print(f'Sum = {max_sum}')
for el in max_sum_list:
    print(*el, sep=' ')