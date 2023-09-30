from functools import reduce


def operate(operator, *args):


    def add():
        return sum(args)

    def subtract():
        result = reduce(lambda a, b: a-b, args)
        return result

    def multiply():
        result = reduce(lambda a, b: a*b, args)
        return result

    def divide():
        result = reduce(lambda a, b: a / b, args)
        return result

    operators = {
        '+': add(),
        '-': subtract(),
        '*': multiply(),
        '/': divide()
                 }

    return operators[operator]

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4, 2))