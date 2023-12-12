from imdb import Cinemagoer

ia = Cinemagoer()
# requesting the code of a movie.
inputMovie = input("Movie's code (after the 'tt' in link): ")
movie = ia.get_movie(inputMovie)

# printing Director/s of the requested movie.
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# printing the genre of the requested movie.
print('Genres: ')
for genre in movie['genres']:
    print(genre)
