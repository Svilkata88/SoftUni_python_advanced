stack = []
num = int(input())

for _ in range(num):
    query = input()
    if query[0] == '1':
        number = query.split()[1]
        stack.append(int(number))
    elif stack:
        if query == '2':
            stack.pop()
        elif query == '3':
            print(max(stack))
        elif query == '4':
            print(min(stack))

while stack:
    print(stack.pop(), end='')
    if stack:
        print(', ', end='')