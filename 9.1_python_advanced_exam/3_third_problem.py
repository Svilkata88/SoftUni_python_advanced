#  Team Lineup

def team_lineup(*args):
    #  1. player_name
    #  2. player_country
    result = {}
    for name, country in args:
        if country not in result:
            result[country] = []
        result[country].append(name)
    sorted_result = sorted(result.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result_str = ''
    for country, players in dict(sorted_result).items():
        result_str += f'{country}:\n'
        for player in players:
            result_str += f'  -{player}\n'
    return result_str

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


