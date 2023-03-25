import spacy

nlp = spacy.load('en_core_web_md')


class Movie:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Description: {self.description}"


movies = []

# read all the movie data from file and insert into a list
def read_movies_data():
    file = open("movies.txt", "r")
    for line in file:
        # data in file is colon separated
        line = line.split(" :")
        movie = Movie(line[0], line[1])

        movies.append(movie)


# give a recommendation on the most similar movie to the one watched by the user
def recommendation(title_watched):
    title_recommended = ""
    highest_score = 0

    watched_movie = get_movie(title_watched)
    nlp_watched = nlp(watched_movie.description)

    for movie in movies:
        # don't compare with same movie
        if movie.title != title_watched:
            nlp_movie = nlp(movie.description)
            score = nlp_watched.similarity(nlp_movie)

            # compare the similarity in watched movie and this movie
            # store movie title and score if it is higher than last most similar movie
            if score > highest_score:
                highest_score = score
                title_recommended = movie.title

    return title_recommended

# return the movie object for the title
def get_movie(title):
    for movie in movies:
        if movie.title == title:
            return movie

# print out all the movies in the list
def display_movies():
    for movie in movies:
        print(movie)

# return true if the movie title is in our list of movies otherwise return false
def movie_valid(title):
    for movie in movies:
        if movie.title == title:
            return True

    return False


# ==========Main Menu=============
while True:
    menu = input('''Select one of the following Options below:

        rmd - read movie data
        r - get recommendation
        dp - display movies
        e - Exit
        : ''').lower()

    if menu == "rmd":
        read_movies_data()

    elif menu == "r":
        movie_watched = input("What is the movie title of the movie you watched?")

        # we only want to find a recommendation for a movie in our list
        if movie_valid(movie_watched):
            print(f"You should watch: {recommendation(movie_watched)}\n")
        else:
            print("ERROR: Movie title not found in list\n")

    elif menu == "dp":
        display_movies()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
