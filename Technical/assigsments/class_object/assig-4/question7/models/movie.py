class Movie:

    def __init__(self, movie_id, movie_name, genre, rating, ticket_price):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.genre = genre
        self.rating = rating
        self.ticket_price = ticket_price

    def display(self):
        print(
            self.movie_id,
            self.movie_name,
            self.genre,
            self.rating,
            self.ticket_price
        )