from models.movie import Movie


movies = []

print("=" * 50)
print("         MOVIE COLLECTION SYSTEM")
print("=" * 50)


for i in range(5):

    print(f"\nEnter details of Movie {i + 1}")

    movie_id = int(input("Enter Movie Id : "))
    movie_name = input("Enter Movie Name : ")
    genre = input("Enter Genre : ")
    rating = float(input("Enter Rating : "))
    ticket_price = float(input("Enter Ticket Price : "))

    movie = Movie(
        movie_id,
        movie_name,
        genre,
        rating,
        ticket_price
    )

    movies.append(movie)


print("\n" + "=" * 50)
print("All Movies:")
print("=" * 50)

for movie in movies:
    movie.display()


print("\nMovies with rating greater than 8:")

for movie in movies:

    if movie.rating > 8:
        print(movie.movie_name, movie.rating)


print("\nAction Movies:")

for movie in movies:

    if movie.genre.lower() == "action":
        print(movie.movie_name)



highest_movie = movies[0]

for movie in movies:

    if movie.rating > highest_movie.rating:
        highest_movie = movie


print("\nHighest Rated Movie:")
print(highest_movie.movie_name, highest_movie.rating)



search_id = int(input("\nSearch Movie Id : "))

found = False

for movie in movies:

    if movie.movie_id == search_id:

        print("\nMovie Found:")
        movie.display()

        found = True
        break

if not found:
    print("\nMovie Not Found")



total_rating = 0

for movie in movies:

    total_rating = total_rating + movie.rating


average_rating = total_rating / len(movies)

print("\nAverage Movie Rating:")
print(round(average_rating, 2))



print("\nMovies with ticket price greater than 300:")

for movie in movies:

    if movie.ticket_price > 300:
        print(movie.movie_name, movie.ticket_price)