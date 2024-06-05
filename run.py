from random import randint

def name_and_rules():
    """"
    function to get user's name and display the rules
    of the game
    """
    player_name = input("enter your name: \n")
    print(f"Let's play battleships, {player_name}")

name_and_rules()