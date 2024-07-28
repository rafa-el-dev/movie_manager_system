class Movie:
    def __init__(self, title, genre, year):
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")

        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}"