import random

from tkinter import *
#label = Label(root, text="YAY! You got one!")
#label.pack()

"""
This is a list of all of the words that the word search uses.
"""
lang_list = [" J A V A S C R I P T ", " R U B Y ", " P Y T H O N ", " H T M L ",
 " C S S ", " R U B Y O N R A I L S ", " H A S S ", " K O T L I N ",
 " G I T H U B ", " D A T A B A S E ", " P R O D U C T I O N ", " C O R N E L L ",
 " G I T L A B "]

"""
Takes a list of strings, agregates them to one string, and prints the string
Precondition:
    - list_arg must be a list of strings
"""
def string_of_list (list_arg):
    l = ""
    for x in lang_list:
        l = l + " " + x
    print(l)

"""This is a list of letters that the word-search uses to fill in the grid"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'h']

"""Picks a random letter from the letters list"""
def pick_random_letter():
    random_int = random.randint(0, 8)
    return letters[random_int]

"""creates a string of letters of the length passed in and returns the
list after converting the string to uppercase.

Precondition: length must be an int.
"""
def make_horizontal_list(length):
    acc = 0
    str_letters = ""
    while acc < length:
        str_letters = str_letters + " " + pick_random_letter()
        acc = acc+1
    return str_letters.upper()

"""
Takes a list and gets rid of all duplicates in the list.

Precondition: list must be a list
"""
def get_rid_of_duplicates(list):
    res = []
    for i in list:
        if i not in res:
            res.append(i)
    return res

"""takes in a list of strings and returns the length of the longest string
in the list.

Precondition: list must be a list of strings.
  """
def find_longest_word(list):
    length = 0
    for i in list:
        if length < len(i):
            length = len(i)
        else:
            length = length
    return length

"""takes a list of words and a nested list that represents the grid.
Returns the nested list after adding the words into it.

Preconditions:
- words_list must be a list of strings.
- crossword must be a nested list of strings
  """
def insert_words_into_list(words_list, crossword):
    number_of_locations = len(words_list)
    row_length = len(crossword[1])
    row_location_list = []
    for i in words_list :
        row_location = random.randint(0, len(crossword)-len(i))
        row_location_list.append(row_location)
        x = " "
        while (x == " "):
            letter_location = random.randint(0, len(crossword[1])-len(i)-5)
            x = crossword[row_location-1][letter_location-1]
        crossword[row_location] = crossword[row_location][0:letter_location] + i + crossword[row_location][0+len(i):]
    return crossword


"""
    - Picks five random words from lang_list and puts them in a list
    - Gets rid of any duplicates in the list
    - finds the length of the longest word
    - calculates row and column lengths
    - creates rows and columns and inserts the words into the grid
    - prints out the grid and returns the nested list representing the
    grid
"""
def main_creation_function():
    word = lang_list[random.randint(0, len(lang_list)-1)]
    word2 = lang_list[random.randint(0, len(lang_list)-1)]
    word3 = lang_list[random.randint(0, len(lang_list)-1)]
    word4 = lang_list[random.randint(0, len(lang_list)-1)]
    word5 = lang_list[random.randint(0, len(lang_list)-1)]
    list = get_rid_of_duplicates([word, word2, word3, word4, word5])
    length = find_longest_word(list)
    row_column_length = length+10
    list_of_rows = []
    i = 0
    while i < row_column_length:
        list_of_rows.append(make_horizontal_list(row_column_length))
        i = i + 1
    list_of_rows = insert_words_into_list(list, list_of_rows)
    for i in list_of_rows:
        if len(i) > row_column_length+30:
            i = i[0:row_column_length+30]
        print(i)
    return list

"""a nested list representing the crossword grid"""
list = main_creation_function()

"""
    - takes the player input and updates it to fit how the words appear on
    the grid.
    - If the player input is in the list of words, it removes it from the
    list and prints different strings depending whether there are more words
    left or if that was the last word.
    - If there are more words left, it also calls itself with the new list
    - If there are no more words left, it does not call itself again.
    - If the player inputs a wrong word, it prints a string asking them to
    try again and calls itself with the same list.

    Precondition:
    - list must be a list of strings
    - player_list must be either empty or a list of strings
"""
def play(list, player_list):
    #print(list)
    player_input = input().upper()

    updated_player_input =" " +  " ".join(player_input) + " "
    if updated_player_input in list:
        list.remove(updated_player_input)
        player_list.append(updated_player_input)
        if list == []:
            print("WooHoo! You've done it!")
        else:
            print("YAY! You got one!")
            play(list, player_list)
    else:
        print("Nooooooo! Try Again!")
        play(list, player_list)

play(list, [])
