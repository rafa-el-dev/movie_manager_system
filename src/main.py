from movie_manager import MovieManager
from movie import Movie

def main():
    manager = MovieManager('../data/movies.csv')
    
    while True:
        print("--- Movie Manager ---\n")
        print("1. List movies")
        print("0. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            manager.list_movies()

        elif choice == '0':
            print("Exit program... Goodbye!")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()