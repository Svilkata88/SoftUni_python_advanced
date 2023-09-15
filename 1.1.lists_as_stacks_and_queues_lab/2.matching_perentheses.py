expression = input()
index_stack = []
results = []

for index in range(len(expression)):
    if expression[index] == '(':
        index_stack.append(index)
    elif expression[index] == ')':
        start_index = index_stack[-1]
        end_index = index + 1
        results.append(expression[start_index:end_index])
        index_stack.pop()

print('\n'.join(results))