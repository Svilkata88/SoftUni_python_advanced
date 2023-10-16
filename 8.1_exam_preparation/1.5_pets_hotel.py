def accommodate_new_pets (hotel_free_capacity, max_weight, *args):
    #  **kwargs - accept 2 arguments: pet's type and pet's weight
    animals_in_the_hotel = {}
    result = ''
    for type_, weight in args:
        if hotel_free_capacity == 0:
            result += 'You did not manage to accommodate all pets!\n'
            break
        if weight <= max_weight:
            if type_ not in animals_in_the_hotel:
                animals_in_the_hotel[type_] = 0
            animals_in_the_hotel[type_] += 1
            hotel_free_capacity -= 1
    else:
        result += f'All pets are accommodated! Available capacity: {hotel_free_capacity}.\n'

    result += 'Accommodated pets:\n'
    for animal, number in sorted(animals_in_the_hotel.items()):
        result += f'{animal}: {number}\n'

    return result

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))

