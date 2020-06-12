import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause('You are lost in the middle of large scary desert!')
    print_pause('Would you go North or South to get out from this desert?')
    print_pause('Enter 1 to go North\nEnter 2 to go South')


def North(animal):  # if the player chose North
    print_pause('You will see fire and a man sitting next to it!')
    print_pause('Will you set or ignore the man and keep wlking?')
    first_choice = input('Enter 1 to set\nEnter 2 to keep walking\n')
    while True:
        if first_choice == '1':
            print_pause('You won!! because the man will tell you how'
                        ' get out from the desert!')
            break
        elif first_choice == '2':
            print_pause('You lost the game!!'
                        ' you will never get out from the desert!')
            break
        else:
            first_choice = input('Enter 1 to set\nEnter 2 to keep walking\n')


def South(animal):  # if the player chose South
    print_pause('You will walk for a while, Then....'
                f' You hear a {random.choice(animal)}\'s voice!')
    # random animal voice
    print_pause('Will you runaway or ignore the'
                ' voice and keep walking slowly?')
    second_choice = input('Enter 1 to Runaway\nEnter 2 to keep walking\n')
    while True:
        if second_choice =='1' or second_choice == '2':
            print_pause('either way you will lose because the'
                        ' animal will follow you and eat you!')
            break
        else:
            second_choice = input('Enter 1 to Runaway\nEnter 2 to keep walking\n')


def choose_direction(animal):
    direction = input('Please enter 1 or 2\n')
    while True:
        if direction == '1':
            North(animal)
            break
        elif direction == '2':
            South(animal)
            break
        elif direction != '1' or direction != '2':
            direction = input('Please enter 1 or 2\n')


def playing_again():
    print_pause('Would you like to play again?')
    play_again = input('Enter Yes or NO\n').lower()
    while True:
        if play_again == 'yes':
            play_game()
        elif play_again == 'no':
            print_pause('I hope you enjoyed the game! see u soon!')
            break
        else:
            play_again = input('Enter Yes or NO\n').lower()


def play_game():
    intro()
    animal = ['bear', 'wolf', 'lion', 'tiger', 'dog']
    choose_direction(animal)
    playing_again()


play_game()
