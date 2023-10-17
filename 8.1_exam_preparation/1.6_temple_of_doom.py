from collections import deque

tools = deque([int(num) for num in input().split()])  # take 1st
substances = [int(num) for num in input().split()]  # take last
challenges = [int(num) for num in input().split()]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
        if not challenges:
            print('Harry found an ostracon, which is dated to the 6th century BCE.')
            break
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)

if challenges:
    print('Harry is lost in the temple. Oblivion awaits him.')

if tools:
    print('Tools: ', end='')
    print(*tools, sep=', ')
if substances:
    print('Substances: ', end='')
    print(*substances, sep=', ')
if challenges:
    print('Challenges: ', end='')
    print(*challenges, sep=', ')
