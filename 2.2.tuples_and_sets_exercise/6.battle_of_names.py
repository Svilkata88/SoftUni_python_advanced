n_names = int(input())
odd_set = set()
even_set = set()
row = 1

for _ in range(n_names):
    name = input()
    total_ch_num = 0
    for ch in name:
        ch_number = ord(ch)
        total_ch_num += ch_number
    total_ch_num = total_ch_num // row
    if total_ch_num % 2 == 0:
        even_set.add(total_ch_num)
    else:
        odd_set.add(total_ch_num)
    row += 1

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=', ')