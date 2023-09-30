def sorting_cheeses(**kwargs):

    sorted_dic = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for k, v in sorted_dic:
        result += f'{k}\n'
        sorted_v = sorted(v, key=lambda kvp: -kvp)
        result += '\n'.join([str(el) for el in sorted_v])
        result += '\n'
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
