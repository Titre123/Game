from random import choice
option_dict = {'R': "Rock", "S": "Scissors", "P": "Paper"}
options = ["R", "S", "P"]

def collect_input():
    choices = True
    while choices:
            inp = input("Enter a letter in the list ['R','S','P']")

            if inp in options:
                choices = False
    user_choice = inp
    comp_choice = choice(["R", "S", "P"])
    print( f'Player {option_dict[user_choice]} : CPU {option_dict[comp_choice]}' )
    return user_choice, comp_choice

def win_lose(user_choice,comp_choice):
    if user_choice == comp_choice:
        gameon = True

    elif user_choice == "R" and comp_choice == "S":
        print("Player win and Computer lose")
        gameon = False
    elif user_choice == "P" and comp_choice == "R":
        print("Player win and Computer lose")
        gameon = False
    elif user_choice == "S" and comp_choice == "P":
        print("Player win and Computer lose")
        gameon = False
    elif user_choice == "S" and comp_choice == "R":
        print("Computer win and Player lose")
        gameon = False
    elif user_choice == "R" and comp_choice == "P":
        print("Computer win and Player lose")
        gameon = False
    elif user_choice == "P" and comp_choice == "S":
        print("Computer win and Player lose")
        gameon = False
    return gameon

user_choice, comp_choice = collect_input()
game_on = win_lose(user_choice, comp_choice)
while game_on:
    user_choice, comp_choice = collect_input()
    game_on = win_lose(user_choice,comp_choice)
