from collections import deque
# read the input sequence
parentheses = deque(input())

# variables
opening = '{[('
closing = '}])'
counter = 0

# logic
while parentheses:
    p = parentheses[0]
    if p in opening:
        matching_index = opening.index(p)
        current_index = parentheses.index(p)
        if parentheses[current_index+1] == closing[matching_index]:
            for _ in range(2):
                parentheses.popleft()
                counter = 0
        else:
            parentheses.rotate(-1)
            counter += 1
    else:
        parentheses.rotate(-1)
        counter += 1
    if counter > len(parentheses) * 2:
        break

# output
if parentheses:
    print('NO')
else:
    print('YES')