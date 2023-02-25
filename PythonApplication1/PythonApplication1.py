def loadMovies(filename):
    #function that will open the file movies.txt and populate a list
    # that will hold all the movie titles in the file
    try:
        with open(filename,'r') as infile:
            movies = [title.strip() for title in infile]
            return movies
    except:
        return []
# Call a function to display all the titles in the list.
def display(movie_list):
    for counter, movie in enumerate(movie_list, start=1):
        print(f'{counter}. {movie}')
# Call a function to add a title to the list.
# Use the list as a parameter passed into the function.
def addMovie(movie_list):
    name = input('Movie: ')
    movie_list.append(name)
    print(f'{name} was added.')

#write the values in the list back to the file movies.txt
def writeToFile(movie_list, filename):
    with open(filename,'w') as outfile:
        for movie in movie_list:
            print(movie,file=outfile)
            
# function deletes a movie from the list
def deleteMovie(movie_list):
    number = int(input('Number: ')) - 1
    if 0 <= number < len(movie_list):
        print(movie_list[number], 'was deleted.')
        del movie_list[number]
    else:
        print('Invalid movie number.')

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

def main():
    filename = 'movies.txt'
    movie_list = loadMovies(filename)
    print('list - List all movies')
    print('add - Add a movie')
    print('del - Delete a movie')
    print('exit - Exit program')

    while True:
        command = input('\nCommand: ').lower()
        if command == 'list': display(movie_list)
        elif command == 'add':
            addMovie(movie_list)
            #write the values in the list back to the file movies.txt.
            writeToFile(movie_list,filename)
        elif command=='del':
            deleteMovie(movie_list)
            # write the values in the list back to the file movies.txt.
            writeToFile(movie_list, filename)
        elif command=='exit': break
        else: print('Not a valid command, Please try again.')
    print('Bye!')
main()