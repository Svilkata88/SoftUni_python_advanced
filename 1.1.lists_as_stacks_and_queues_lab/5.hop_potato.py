from collections import deque

kids = input().split()
n_toss = int(input())
kids = deque(kids)

count = 0

while len(kids) > 1:
    for index in range(n_toss):
        kids.rotate(-1)
        if index == n_toss-1:
            print(f'Removed {kids.pop()}')

print(f'Last is {kids[0]}')