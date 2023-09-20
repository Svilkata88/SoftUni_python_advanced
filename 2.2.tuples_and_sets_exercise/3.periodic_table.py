n_inputs = int(input())
uniques_compounds = set()

for _ in range(n_inputs):
    compounds = set(input().split())
    uniques_compounds.update(compounds)

print(*uniques_compounds, sep='\n')