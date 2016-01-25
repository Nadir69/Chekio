import media
import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1h 30min")

avatar = media.Movie("Avatar",
                     "A story about blue cats",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "1h 40min")

planet_of_the_apes = media.Movie("Planet of the apes",
                                 "A story of brave monkeys",
                                 "https://upload.wikimedia.org/wikipedia/en/7/77/Dawn_of_the_Planet_of_the_Apes.jpg",
                                 "https://www.youtube.com/watch?v=3sHMCRaS3ao",
                                 "1h 50min")

hackers = media.Movie("Hackers",
                      "Their crime is curiosity",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                      "https://www.youtube.com/watch?v=Ql1uLyuWra8",
                      "2h 00min")

matrix = media.Movie("The Martix",
                     "Computer programmer Neo learns the truth",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                     "2h 10min")

snatch = media.Movie("Snatch",
                     "A story about boxing, gypsies and diamonds",
                     "http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1_SX640_SY720_.jpg",
                     "https://www.youtube.com/watch?v=Q8jbt0wBkMI",
                     "2h 20min")

movies = [toy_story, avatar, planet_of_the_apes, hackers, matrix, snatch]
# fresh_tomatoes.open_movies_page(movies)
# print planet_of_the_apes.trailer
# planet_of_the_apes.show_trailer()
# print media.Movie.VALID_RATINGS
# print media.Movie.__doc__
# print media.Movie.__module__
# print media.Movie.__name__

print toy_story.duration