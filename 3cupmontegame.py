# 3 cup monte using Python.
# uing a list to represen the 3 cups and the character "O" as the ball

choose_a_cup_list = ['','O','']

#import random method to shuffle the list.
from random import shuffle

#function that randomizes the list chose_a_cup_list
def shuffle_list(choose_a_cup_list):
    shuffle(choose_a_cup_list)
    return choose_a_cup_list

#fucntion that collects users input.
def player_choice():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Enter a number between 0, 1, or 2: ")

    return int(guess)

#function that checks if player answer is right or wrong
def check_choice(choose_a_cup_list,player_choice):
    if choose_a_cup_list[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong choice !')
        print(choose_a_cup_list)

#shuffled list
mixedlist = shuffle_list(choose_a_cup_list)

#user choice
guess = player_choice()

#check answer
check_choice(mixedlist,guess)
