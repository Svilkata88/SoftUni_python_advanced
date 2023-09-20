sets_length = [int(num) for num in input().split()]
n = set()
m = set()

for index in range(sum(sets_length)):
    if index < sets_length[0]:
        num = int(input())
        n.add(num)
    elif index >= sets_length[0]:
        num = int(input())
        m.add(num)

unique_num_both_sets = n.intersection(m)
print(*unique_num_both_sets, sep='\n')
