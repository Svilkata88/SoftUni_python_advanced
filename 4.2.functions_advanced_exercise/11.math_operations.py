from collections import deque


def math_operations(*args, **kwargs):
    keys = deque([1,2,3,4])
    numbers = deque(args)
    my_dict = {**kwargs}
    def add(num):
        my_dict['a'] += num
    def subtract(num):
        my_dict['s'] -= num
    def divide(num):
        if num > 0:
            my_dict['d'] /= num
    def multiply(num):
        my_dict['m'] *= num

    actions = {
        1: add,
        2: subtract,
        3: divide,
        4: multiply
            }

    while numbers:
        num = numbers.popleft()
        actions[keys[0]](num)
        keys.rotate(-1)

    final_result = []
    result = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
    for letter, value in result.items():
        final_result.append(f'{letter}: {value:.1f}')

    return '\n'.join(final_result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))

