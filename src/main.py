from movie_manager import MovieManager
from movie import Movie

def main():
    manager = MovieManager('../data/movies.csv')
    
    while True:
        print("--- Movie Manager ---\n")
        print("1. List movies")
        print("2. Add movie")
        print("0. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            manager.list_movies()
            
        elif choice == '2':
            title = input("Enter title: ")
            genre = input("Enter genre: ")
            year = int(input("Enter year: "))
            if not title or not genre or not year:
                print("All fields (Title, Genre, Year) are mandatory. Try again.")
            else:
                movie = Movie(title, genre, year)
                manager.add_movie(movie)
                print(f"Movie '{title}' added successfully!")

        elif choice == '0':
            print("Exit program... Goodbye!")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()