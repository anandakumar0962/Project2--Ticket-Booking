movies = []
class Movies:
    
    def __init__(self):
        self.movies = movies
    
    def display_movies(self):
        print("--------------------------------------------------------\n")
        for movie in self.movies:
            print(movie.movie_id, '\t', movie.movie_name, '\t', movie.duration, '\t', movie.rating)

    def select_movie(self):
        self.display_movies()
        movie_id = int(input("\nEnter a movie id:\n"))
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie.movie_name

class MoviesData:

    def __init__(self,movie_id:int, movie_name:str, duration:str, rating:float):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.duration = duration
        self.rating = rating

movie1 = MoviesData(1, 'Por Thozhil','2hr 27mins', 7.5)
movie2 = MoviesData(2, 'Good Night','2hr 22mins', 7.7)
movie3 = MoviesData(3, 'Leo       ','2hr 39mins', 8.1)

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
