def age_assignment(*args, **kwargs):
    names = args
    results = []
    for letter, age in kwargs.items():
        for name in args:
            if name[0] == letter:
                results.append(f'{name} is {age} years old.')

    return '\n'.join(sorted(results))



print(age_assignment("Peter", "George", G=26, P=19))