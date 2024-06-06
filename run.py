from random import randint


class Board:
    """
    class for the game boards
    """
    def __init__(self, size):
        self.board = board
        self.size = size
        self.board = [["~" for x in range(size)] for y in range(size)]

    def print_board(self):
        """
        function to print the boards to the terminal
        """
        print("0 1 2 3 4")
        print("~~~~~")
        
        


def name_and_rules():
    """"
    function to get user's name and display the rules
    of the game
    """
    player_name = input("enter your name: \n")
    print("Objective: sink all of the computer's ships first\n")
    print("Guess a row between 0 - 4")
    print("Guess a column between 0 -4\n")

    print(f"Let's play battleships, {player_name}, good luck!")



name_and_rules()
Board()