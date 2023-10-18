from collections import deque

textiles = deque(int(num) for num in input().split())
medicaments = [int(num) for num in input().split()]
healing_items = []

item_resources_needed = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit',
}

while textiles and medicaments:
    first_textile = textiles.popleft()
    first_medicament = medicaments.pop()
    current_sum = first_medicament + first_textile
    if current_sum in item_resources_needed:
        healing_items.append(item_resources_needed[current_sum])
    elif current_sum > 100:
        healing_items.append(item_resources_needed[100])
        current_sum -= 100
        medicaments[-1] += current_sum
    else:
        medicaments.append(first_medicament + 10)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')

if healing_items:
    items_dict = {}
    for el in healing_items:
        if el not in items_dict:
            items_dict[el] = healing_items.count(el)
    sorted_items = sorted(items_dict.items(), key=lambda items: (-items[1], items[0]))
    for item, count in dict(sorted_items).items():
        print(f'{item} - {count}')

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join([str(el) for el in medicaments])}")
elif textiles:
    print(f"Textiles left: {', '.join([str(el) for el in textiles])}")



