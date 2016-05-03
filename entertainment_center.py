import fresh_tomatoes
import media

# Creed
creed = media.Movie("Creed",
                        "https://upload.wikimedia.org/wikipedia/en/2/24/Creed_poster.jpg",
                        "https://www.youtube.com/watch?v=Uv554B7YHk4")

# Matrix
matrix = media.Movie("Matrix",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Spiderman
spiderman = media.Movie("Spiderman",
                             "https://www.movieposter.com/posters/archive/main/21/MPW-10583",
                             "https://www.youtube.com/watch?v=EQdOOTQnuvk")



# Build website
movies = [creed, matrix, spiderman]
          

fresh_tomatoes.open_movies_page(movies)