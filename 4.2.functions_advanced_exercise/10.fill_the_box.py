def fill_the_box(*args):
    cube = 1

    for i in range(len(args)):
        if args[i] == 'Finish':
            if cube > 0:
                return f'There is free space in the box. You could put {cube} more cubes.'
            return f'No more free space! You have {abs(cube)} more cubes.'
        elif i < 3:
            cube *= args[i]
        else:
            cube -= args[i]


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))