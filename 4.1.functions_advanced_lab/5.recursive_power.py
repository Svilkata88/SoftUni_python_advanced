def recursive_power(num1 , power):
    if power == 1:
        return num1
    return num1 * recursive_power(num1, power-1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))