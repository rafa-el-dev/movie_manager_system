import csv
from movie import Movie

class MovieManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.movies = self.load_movies()

    def load_movies(self):
        movies = []
        try:
            with open(self.data_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row.get('title')
                    genre = row.get('genre')
                    year = row.get('year')
                    if title and genre and year:
                        movie = Movie(title, genre, year)
                        movies.append(movie)
                    else:
                        print("Error reading line from CSV: Missing data")
        except FileNotFoundError:
            print(f"File {self.data_file} not found.")
        except csv.Error as e:
            print(f"Error loading CSV file: {e}")
        except Exception as e:
            print(f"An unknown error occurred while loading the CSV file: {e}")
        return movies

    def list_movies(self):
        for movie in self.movies:
            print(movie)