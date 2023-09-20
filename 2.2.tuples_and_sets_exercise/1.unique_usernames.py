n_names = int(input())
unique_names = set()

for _ in range(n_names):
    name = input()
    unique_names.add(name)

print(*unique_names, sep='\n')
