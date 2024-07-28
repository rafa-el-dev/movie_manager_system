class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}"