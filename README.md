Movie Manager Application
=========================

Overview
--------

The Movie Manager Application is a command-line tool designed to help users manage a collection of movies. It allows users to list, add, remove, edit, search, sort, and export movies. The application operates on a CSV file that stores movie details such as title, genre, and year of release.

⚙️ Features
--------

-   **List Movies**: Display all movies in the collection.
-   **Add Movie**: Add a new movie to the collection.
-   **Remove Movie**: Remove a movie from the collection by its index.
-   **Edit Movie**: Edit the details of an existing movie.
-   **Search Movie**: Search for movies by title, genre, or year.
-   **Sort Movies**: Sort movies by title, genre, or year.
-   **Export Movies**: Export the movie list to a CSV file.

💎 Value for Users
---------------

This application provides a straightforward way to manage a personal movie collection. It can be particularly useful for movie enthusiasts who want to keep track of their movies and easily search or sort them based on different criteria.

 💻 Installation
------------

1.  Clone the repository or download the files.
2.  Ensure you have Python installed on your system (Python 3.6+ recommended).
3.  Place the `movies.csv` file in the appropriate directory as referenced in `main.py`.

Usage
-----

### 🚀 Running the Application

To start the Movie Manager Application, run the following command in your terminal:

```
  python3 main.py
 ```


### Main Menu Options

Once the application is running, you will see the following menu:

```
--- Movie Manager ---

1. List movies
2. Add movie
3. Remove movie
4. Edit movie
5. Search movie
6. Sort movies
7. Export movies
0. Exit`
```

You can select an option by entering the corresponding number.

### Commands

#### 1\. List Movies

Displays all movies currently in the collection.

#### 2\. Add Movie

Prompts you to enter the title, genre, and year of the new movie. All fields are mandatory.

#### 3\. Remove Movie

Displays a list of movies with their indices and prompts you to enter the index of the movie you wish to remove.

#### 4\. Edit Movie

Displays a list of movies with their indices and prompts you to enter the index of the movie you wish to edit. Then, you can update the title, genre, and year of the movie.

#### 5\. Search Movie

Prompts you to enter a search term and displays movies that match the term in their title, genre, or year.

#### 6\. Sort Movies

Prompts you to select a criterion for sorting the movies:

-   `1`: Sort by title
-   `2`: Sort by genre
-   `3`: Sort by year

#### 7\. Export Movies

Exports the movie list to a specified CSV file.

#### 0\. Exit

Exits the application.

File Descriptions
-----------------

### `main.py`

This is the entry point of the application. It initializes the `MovieManager` and handles user input to perform various movie management operations.

### `movie_manager.py`

Contains the `MovieManager` class, which provides methods to list, add, remove, edit, search, sort, and export movies.

### `movie.py`

Defines the `Movie` class, which represents a movie with a title, genre, and year. It includes validation to ensure the title is a non-empty string.

### `movies.csv`

A CSV file that stores the initial movie data. Each row represents a movie with columns for title, genre, and year.

Example
-------

Below is an example of how to run the application and use some of its features:

```
`$ python3 main.py
--- Movie Manager ---

1. List movies
2. Add movie
3. Remove movie
4. Edit movie
5. Search movie
6. Sort movies
7. Export movies
0. Exit
Choose an option: 1

1. Inception (2010) - Sci-Fi
2. The Matrix (1999) - Sci-Fi
3. Interstellar (2014) - Sci-Fi
...
```
🔧 Manual Tests Performed
-------

To ensure correct performance and good performance of the application, several manual tests were performed covering the main functionalities of Movie Manager:

#### Movie Listing Test

- **Description**: Verified whether the listing displays all movies correctly.

#### Movie Addition Test

- **Description**: Tested the addition of new movies.

#### Movie Removal Test

- **Description**: Verified whether movie removal works correctly.

#### Movie Editing Test

- **Description**: Evaluated the editing functionality.

#### Movie Search Test

- **Description**: Tested the movie search to ensure correct results.

#### Movie Sorting Test

- **Description**: Evaluated the sorting functionality.

#### Movie Export Test

- **Description**: Tested the export of the movie list.

### Final Considerations

The manual tests performed demonstrated that the Movie Manager application works as expected, with good performance and without significant errors during the main operations. These tests ensure that users can manage their movie collections efficiently and reliably.

## 📫 Suggestions

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or create a pull request. For major changes, please open an issue first to discuss the proposed changes.


📝 License
-------

This project is licensed under the MIT License.

----------