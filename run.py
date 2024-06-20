import random


class Board:
    """
    class for the game boards
    """

    def __init__(self, size, num_ships, type):
        self.size = size
        self.board = [["~" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.type = type

    def print_board(self, hide_ships = False):
        """
        function to print the boards to the terminal
        rows and columns start at 1 for a more user friendly experience
        """
        print("  " + " ".join(str(x) for x in range(1, self.size + 1)))
        for row_number, row in enumerate(self.board, start=1):
            display_row = ['~' if hide_ships and cell == 'O' else cell for cell in row]
            print(f"{row_number} {' '.join(display_row)}")


def name_and_rules():
    """"
    function to get user's name and display the rules
    of the game
    """
    player_name = input("enter your name: \n")
    print("Objective: sink all of the computer's ships first\n")
    print("Guess a row between 0 - 4")
    print("Guess a column between 0 - 4\n")

    print(f"Let's play battleships, {player_name}, good luck!")


class Play:
    def __init__(self, board):
        self.board = board

    def add_ships(self):
        """
        Function to add ships randomly to game boards
        """
        size = self.board.size
        placed_ships = 0
    
        while placed_ships < self.board.num_ships:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
        
            if self.board.board[row][col] == '~':
                self.board.board[row][col] = 'O'
                placed_ships += 1
    
    
    def validate_guess():
        """
        function to validate a player's input
        """


    def play_battleships(player_board, comp_board):
        """
        function to make a move
        """

        while player_board.hits < player_board.num_ships and comp_board.hits < comp_board.num_ships:
            print("guess a row: predict a number between 1 - 5")
            guess_row = input("row number:")
            print("guess a column: predict a number between 1 - 5")
            guess_column = input("column number:")

        if guess_row == row and guess_column == col:
            print("HIT!")
        else:
            if (guess_row < 1 or guess_row > 5) or (guess_column < 1 or guess_column > 5):
                print("please guess a number between 1 - 5\n")
                


size = 5
num_ships = 3


player_board = Board(size, num_ships, "Player")
comp_board = Board(size, num_ships, "Computer")


player_game = Play(player_board)
comp_game = Play(comp_board)


name_and_rules()

player_game.add_ships()
comp_game.add_ships()



print("\nPlayer's Board:")
player_board.print_board(hide_ships=False)
print("\nComputer's Board:")
comp_board.print_board(hide_ships=True)

