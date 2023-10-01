def concatenate(*args, **kwargs):

    new_string = ''.join(args)
    for key, element in kwargs.items():
        if key in new_string:
            new_string = new_string.replace(key, element)

    return new_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))