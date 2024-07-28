from movie_manager import MovieManager
from movie import Movie

def main():
    manager = MovieManager('../data/movies.csv')
    
    while True:
        print("--- Movie Manager ---\n")
        print("1. List movies")
        print("2. Add movie")
        print("3. Remove movie")
        print("4. Edit movie")
        print("5. Search movie")
        print("0. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            manager.list_movies()

        elif choice == '2':
            title = input("Enter title: ").strip()
            genre = input("Enter genre: ").strip()
            year = int(input("Enter year: "))
            if not title or not genre or not year:
                print("All fields (Title, Genre, Year) are mandatory. Try again.")
            else:
                movie = Movie(title, genre, year)
                manager.add_movie(movie)
                print(f"Movie '{title}' added successfully!")

        elif choice == '3':
            manager.list_movies()
            try:
                index = int(input("Index of the movie to be removed: "))
                manager.remove_movie(index)
            except ValueError:
                print("Please enter a valid number. Try again.")

        elif choice == '4':
            manager.list_movies()
            try:
                index = int(input("Index of the movie to be edited: "))
                new_title = input("Enter new title: ").strip()
                new_genre = input("Enter new genre: ").strip()
                new_year = int(input("Enter new year: "))
                if not new_title or not new_genre or not new_year:
                    print("All fields (Title, Genre, Year) are mandatory. Try again.")
                else:
                    manager.edit_movie(index, new_title, new_genre, new_year)
            except ValueError:
                print("Please enter a valid number. Try again.")

        elif choice == '5':
            term = input("Enter the term to be searched (title, genre or year): ").strip()
            if not term:
                print("Search term cannot be empty. Try again.")
            else:
                manager.search_movie(term)

        elif choice == '0':
            print("Exit program... Goodbye!")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()