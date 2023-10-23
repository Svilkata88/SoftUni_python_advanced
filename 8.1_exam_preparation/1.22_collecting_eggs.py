from collections import deque

eggs = deque(list(map(int, input().split(', '))))  # first egg
pieces_of_paper = deque(list(map(int, input().split(', '))))  # last paper
eggs_in_the_box = 0

while eggs and pieces_of_paper:
    if eggs[0] <= 0:
        current_egg = eggs.popleft()
        continue
    if eggs[0] == 13:
        eggs.popleft()
        swap_1 = pieces_of_paper.pop()
        swap_2 = pieces_of_paper.popleft()
        pieces_of_paper.appendleft(swap_1)
        pieces_of_paper.append(swap_2)
        continue
    current_egg = eggs.popleft()
    current_paper = pieces_of_paper.pop()
    current_sum = current_egg + current_paper

    if current_egg == 13:
        pieces_of_paper.appendleft(pieces_of_paper.pop())
        pieces_of_paper.append(pieces_of_paper.pop())

    elif current_sum <= 50:
        eggs_in_the_box += 1

if eggs_in_the_box > 0:
    print(f'Great! You filled {eggs_in_the_box} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(str(egg) for egg in eggs)}')
if pieces_of_paper:
    print(f'Pieces of paper left: {", ".join(str(piece) for piece in pieces_of_paper)}')

