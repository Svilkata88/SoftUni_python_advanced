def shop_from_grocery_list(budget, grocery_list, *args):
    #  budget: int
    #  grocery_list: list of one, many or no strings
    #  two el. tuple: 1st - product name (str), 2nd - price (flot)
    product_bought = []
    for product_name, price in args:
        if product_name in grocery_list and product_name not in product_bought:
            if budget >= price:
                budget -= price
                product_bought.append(product_name)
            else:
                break

    for product in grocery_list:
        if product in product_bought:
            continue
        else:
            result = ''
            result += 'You did not buy all the products. Missing products: '
            for p in product_bought:
                if p in grocery_list:
                    grocery_list.remove(p)
            result += ', '.join(grocery_list) + '.'
            return result
    else:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


