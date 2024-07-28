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
        if not self.movies:
            print("No movies registered.")
        else:
            for index, movie in enumerate(self.movies, start=1):
                print(f"{index}. {movie}")

    def add_movie(self, movie):
        self.movies.append(movie)
        self.save_movies()

    def save_movies(self):
        with open(self.data_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'genre', 'year'])
            for movie in self.movies:
                writer.writerow([movie.title, movie.genre, movie.year])

    def remove_movie(self, index):
        if 1 <= index <= len(self.movies):
            removed_movie = self.movies.pop(index - 1)
            self.save_movies()
            print(f"Movie '{removed_movie.title}' successfully removed!")
        else:
            print("Invalid index. Please try again.")

    def edit_movie(self, index, new_title, new_genre, new_year):
        if 1 <= index <= len(self.movies):
            movie = self.movies[index - 1]
            movie.title = new_title
            movie.genre = new_genre
            movie.year = new_year
            self.save_movies()
            print(f"Movie edited successfully!")
        else:
            print("Invalid index. Please try again.")

    def search_movie(self, term):
        term_lower = term.lower()
        found_movies = [movie for movie in self.movies 
                        if term_lower in movie.title.lower() 
                        or term_lower in movie.genre.lower() 
                        or term_lower in movie.year.lower()]
        if found_movies:
            for movie in found_movies:
                print(movie)
        else:
            print(f"No movies found with the term '{term}'.")