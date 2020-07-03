"""
Replace the contents of this module docstring with your own details
Name:
Date started:23/4/2020
GitHub URL:https://github.com/JCUS-CP1404/assignment-01-songs-app-minhquan0902
"""

''''Here are the global lists which will be used in the function, also the command to open the songs.csv file. I 
import csv library just in case i have to use some of its function to interact with the csv file. one important list 
to notice is the FILE_LIST in which will store all valuable data from main_menu(), list_function, add_function() and 
learnt_function() '''
import csv

REMAINDER = [1]
TOTAL_SONG = [0]
song_list = open('songs.csv', 'r')
FILE_LIST = song_list.readlines()

'''This is the main function of the program, here the main_menu function is triggered, lead the users to the main 
menu for interaction.  '''


def main():
    """..."""
    print("Songs to Learn 1.0 - by Quan Nguyen")
    main_menu()


'''The main_menu function will display the options for users to choose and go directly to the three main functions, 
show lists (L), complete a song(C), add a song(A) and Quit(Q). After interacting with the programs, the Quit option 
will save all changes and then write to the songs.csv file '''


def main_menu():
    print("Menu:")
    count_load = 0
    for lines in FILE_LIST:
        count_load += 1
    print(count_load, "songs loaded")

    print("L - List songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")
    menu = input(">>>").upper()
    while menu not in ["L", "A", "C", "Q"]:
        menu = input("Invalid, please re-enter and appropriate option: ").upper()
    if menu == "L":
        list_function()
    if menu == "A":
        add_function()
    if menu == "C":
        learnt_function()
    else:
        confirm = input("Are you sure you want to quit? -(Y)es, (N)o ").upper()
        while confirm not in ["Y", "N"]:
            confirm = input("Invalid, please re-enter your option: (Y)es or (N)o").upper()
        if confirm == "Y":
            with open('songs.csv', 'w') as song_list:
                for item in FILE_LIST:
                    song_list.write("{}".format(item))
            print("----Saving to your csv file----")
            print("-- Exited playlist. Have a nice day! --")
            quit()
        else:
            main_menu()


'''list_function show all the current songs and its status(learned or need to be learn). All the data read inside the 
CSV files will be store inside a list for interaction and then write back to the csv file after all interactions are 
done. Because it is difficult to interact directly with the csv file through read and write command of Python, 
so i create a list (FILE_LIST) and import all csv data to it, users will interact and change the value inside the 
list and then after the program is closed, data inside the list will be writen it back to the csv file '''


def list_function():
    count = 0
    count_learnt = 0

    list = []
    for lines in FILE_LIST:
        count += 1
        new_lines = lines.split(',')
        input_song = new_lines[0]
        input_artist = new_lines[1]
        input_year = new_lines[2]
        learn = new_lines[3].replace("l", "*").replace("u", "").replace("\n", "")
        list.append(count)
        songs_display = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(count, learn, input_song, input_artist, input_year))
        print(songs_display)

        if "*" in learn:
            count_learnt += 1
    print("-" * 100)
    print("Total songs loaded: ", max(list))
    count_need = (max(list) - count_learnt)
    REMAINDER.append(count_need)
    print(max(list) - count_learnt, "songs still to learn")
    print(count_learnt, "songs learned")
    TOTAL_SONG.append(max(list))
    print("-" * 100)
    main_menu()


'''' add_function allows users too add more songs to the FILE_LIST list, so later on it can be displayed and 
formatted in the list_function() function '''


def add_function():
    learn_status = "u\n"
    title = input("Title: ")
    while title == "":
        print("Input can not be blank")
        title = input("Title: ")
    artist = input("Artist: ")
    while artist == "":
        print("Input can not be blank")
        artist = input("Artist: ")
    test = True
    while test == True:
        try:
            year = int(input("Year: "))
            test = False
        except ValueError:
            print("Invalid input; enter a valid number")
    while year < 0:
        print("Number must be >= 0")
        test = True
        while test == True:
            try:
                year = int(input("Year: "))
                test = False
            except ValueError:
                print("Invalid input; enter a valid number")

    if REMAINDER[-1] == 0:
        REMAINDER.remove(REMAINDER[-1])
    final_result = ("{},{},{},{}".format(title, artist, year, learn_status))
    FILE_LIST.append(final_result)
    print("{} by {} from ({}) added to song list".format(title, artist, year))
    print('-' * 100)
    main_menu()


''''Learnt_function() allows user to mark the completed songs. If all the songs are marked complete, there will be 
the print to show that there are no more songs to learn '''


def learnt_function():
    learn_status = "l\n"
    if min(REMAINDER) == 0:
        print('-' * 100)
        print("No more songs to learn!")
        print('-' * 100)
        main_menu()

    test = True
    while test == True:
        try:
            number = int(input("Enter the number of a song to be marked as learnt: "))
            test = False
        except ValueError:
            print("Invalid input, please enter a number")
    if max(TOTAL_SONG) == 0:
        print("-" * 100)
        print("Please load the list of songs first by type in L in the main menu")
        print("Remember to load the list song for checking every time you make a change")
        print("-" * 100)
        main_menu()

    while number > max(TOTAL_SONG) or number <= 0:
        print("Please input the appropriate value!")
        number = int(input("Enter the number of the song to be marked as learnt: "))

    rows = FILE_LIST[number - 1]
    new_list_rows = rows.split(",")
    song_name = new_list_rows[0]
    artist_name = new_list_rows[1]
    year = new_list_rows[2]
    result = ("{},{},{},{}".format(song_name, artist_name, year, learn_status))
    result_1 = ("'{} by {} from {}' is marked learnt! Congratulation!".format(song_name, artist_name, year))
    FILE_LIST.append(result)
    FILE_LIST.remove(FILE_LIST[number - 1])
    print(result_1)
    print("Remember to load the list song for checking every time you make a change")
    print('-' * 100)
    main_menu()


if __name__ == '__main__':
    main()
