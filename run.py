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

    def print_board(self):
        """
        function to print the boards to the terminal
        rows and columns start at 1 for a more user friendly experience
        """
        print("  " + " ".join(str(x) for x in range(1, self.size + 1)))
        for row_number, row in enumerate(self.board, start=1):
            print(f"{row_number} {' '.join(row)}")


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
player_board.print_board()
print("\nComputer's Board:")
comp_board.print_board()

