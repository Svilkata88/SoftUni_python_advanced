from collections import deque
string = input().split()
result = deque()

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for ch in string:
    if ch not in operators and ch != ' ':
        result.append(int(ch))
    elif ch in operators:
        while len(result) > 1:
            first_number = result.popleft()
            second_number = result.popleft()
            if ch == '+':
                result.appendleft(operators['+'](first_number, second_number))
            elif ch == '-':
                result.appendleft(operators['-'](first_number, second_number))
            elif ch == '*':
                result.appendleft(operators['*'](first_number, second_number))
            elif ch == '/':
                result.appendleft(operators['/'](first_number, second_number))

print(result[0])