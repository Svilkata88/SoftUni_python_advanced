rows, cols = [int(num) for num in input().split()]

start_letter = 97

for row in range(rows):
    for col in range(cols):
        element = f'{chr(start_letter)}{chr(start_letter+col)}{chr(start_letter)}'
        print(element, end=' ')
    start_letter += 1
    print()