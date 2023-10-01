def even_odd_filter(**kwargs):
    my_dict = {}

    def even_or_odd():
        if key == 'even':
            my_dict.update({key: list(filter(lambda x: x % 2 == 0, value))})
        elif key == 'odd':
            my_dict.update({key: list(filter(lambda x: x % 2 != 0, value))})

    for key, value in kwargs.items():
        even_or_odd()

    return dict(sorted(my_dict.items(), key=lambda x:-len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
