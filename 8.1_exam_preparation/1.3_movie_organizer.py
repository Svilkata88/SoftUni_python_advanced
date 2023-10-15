def movie_organizer(*args):
    movies = {}
    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    sorted_movies = sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for genre, movies in dict(sorted_movies).items():
        result += f'{genre} - {len(movies)}\n'
        for el in sorted(movies):
            result += f'* {el}\n'
    return result


print(movie_organizer(("The Matrix", "Sci-fi")))



