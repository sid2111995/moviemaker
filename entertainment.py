import fresh_tomatoes
import media
import urllib

# Add Movies variables and Links to Youtube trailers below

toy_story = media.Movie("Toy story",
                        "A story of boy whos toys comes to life",
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on Spaceship",
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
dangal = media.Movie("Dangal",
                     "A story of 2 girls winning gold medal",
                     "Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")
znmd = media.Movie("ZNMD",
                   "4 friends on a holiday",
                   "Zindaginamilegidobara.jpg",
                   "https://www.youtube.com/watch?v=ifIBOKCfjVs")
notebook = media.Movie("Notebook",
                       "Love story of 2 people",
                       "Posternotebook.jpg",
                       "https://www.youtube.com/watch?v=FC6biTjEyZw")
nowucme = media.Movie("Now U see me",
                      "Story of magicians",
                      "Now_You_See_Me_Poster.jpg",
                      "https://www.youtube.com/watch?v=KzJNYYkkhzc")

# Save all movies variables to a array of movies

movies = [toy_story, avatar, dangal, znmd, notebook, nowucme]
fresh_tomatoes.open_movies_page(movies)
