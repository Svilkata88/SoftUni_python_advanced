n_lines = int(input())
ranges = []
longest_intersection = set()

for _ in range(n_lines):
    range1, range2 = input().split('-')
    ranges.append((range1, range2))


for tuple_n in ranges:
    intersection = set()
    current_set = set()
    for range_n in tuple_n:
        start_i, end_i = range_n.split(',')
        start_i = int(start_i)
        end_i = int(end_i)
        for num in range(start_i, end_i+1):
            current_set.add(num)
        if not intersection:
            intersection = current_set
            current_set = set()
        else:
            intersection = intersection.intersection(current_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {[*longest_intersection]} with length {len(longest_intersection)}')

