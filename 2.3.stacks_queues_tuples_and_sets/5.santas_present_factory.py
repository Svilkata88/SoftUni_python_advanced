from collections import deque

materials = deque([int(material) for material in input().split()]) # last
magic_level = deque([int(level) for level in input().split()]) # first
crafted_presents = {}

presents = {
150: "Doll",
250: "Wooden train",
300: "Teddy bear",
400: "Bicycle"
}


while materials and magic_level:
    total_magic = materials[-1] * magic_level[0]

    if total_magic in presents:
        present = presents[total_magic]
        if present not in crafted_presents:
            crafted_presents[present] = 0
        crafted_presents[present] += 1
        materials.pop()
        magic_level.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif total_magic > 0:
        magic_level.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic_level[0] == 0:
        materials.pop()
        magic_level.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic_level[0] == 0:
        magic_level.popleft()

if ('Doll' in crafted_presents and 'Wooden train' in crafted_presents)\
        or ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials:
    print(f"Materials left: ", end='')
    materials.reverse()
    print(*materials, sep=', ')
if magic_level:
    print(f"Magic left: {', '.join([str(magic) for magic in magic_level])}")
for present, count in sorted(crafted_presents.items()):
    print(f'{present}: {count}')
