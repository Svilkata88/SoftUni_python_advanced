from collections import deque

working_bees = deque([int(bees) for bees in input().split()])
nectars = [int(nectar) for nectar in input().split()]
symbols = deque(input().strip().split())
total_honey_made = 0
symbol_operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

while working_bees and nectars:
    if working_bees[0] <= nectars[-1]:
        bee_returned_home = working_bees.popleft()
        nectar_taken = nectars.pop()
    else:
        nectars.pop()
        continue
    current_symbol = symbols.popleft()
    if current_symbol == '/' and nectar_taken == 0:
        continue
    else:
        honey_result = abs(symbol_operations[current_symbol](bee_returned_home, nectar_taken))
        total_honey_made += honey_result


print(f'Total honey made: {total_honey_made}')
if working_bees:
    print(f'Bees left: ', end='')
    print(*working_bees, sep=', ')
if nectars:
    print(f'Nectar left: ', end='')
    print(*nectars, sep=', ')