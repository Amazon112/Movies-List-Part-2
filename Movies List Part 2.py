def write_movies(movies):
    with open(filename, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")    

def read_movies():
    movies = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies   

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()
  
def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(index - 1)
        write_movies(movies)
        print(f"{movie} was deleted.\n")
        
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

def main()
def main(filename, movie_list):
    while True:
        command = main()
        command = input('\nCommand: ').lower()
        return command
        if command == 'list': display(movie_list)
        elif command == 'add':
            addMovie(movie_list)
            writeToFile(movie_list,filename)
        elif command=='del':
            deleteMovie(movie_list)
            writeToFile(movie_list, filename)
        elif command=='exit': break
        else: print('Not a valid command, Please try again.')

def main():
    filename = 'movies.txt'
    movie_list = loadMovies(filename)
    print('list - List all movies')
    print('add - Add a movie')
    print('del - Delete a movie')
    print('exit - Exit program')
    
    return main(filename, movie_list)
    print('Bye!')
main()