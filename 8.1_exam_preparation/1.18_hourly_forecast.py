from collections import OrderedDict


def forecast(*args):
    # args: 2 tuple pair: first one is location, second one is weather
    weather_dict = OrderedDict()
    dict_ = {}
    # adding the weather and it's locations in the preliminary unordered dict!
    for location, weather in args:
        if weather not in dict_:
            dict_[weather] = []
        dict_[weather].append(location)

    # checking if the every weather is in the first dict!
    # If not we don't make key/value pair for it in the new ordered dict!
    weather_dict['Sunny'] = sorted(dict_['Sunny']) if 'Sunny' in dict_ else ''
    weather_dict['Cloudy'] = sorted(dict_['Cloudy']) if 'Cloudy' in dict_ else ''
    weather_dict['Rainy'] = sorted(dict_['Rainy']) if 'Rainy' in dict_ else ''

    # preparing the result string and return it!
    result = ''
    for weather, loc in weather_dict.items():
        for city in loc:
            result += f'{city} - {weather}\n'
    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

