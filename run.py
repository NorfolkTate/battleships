import random


class Board:
    """
    class for the game boards
    """

    def __init__(self, size, num_ships, type):
        self.size = size
        self.board = [["~" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.hits = 0
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

    def get_guess(self, row, col):
        """
        function to get and process a guess
        """
        if self.board[row][col] == 'O':
            self.board[row][col] = 'X' 
            self.hits += 1
            return True
        elif self.board[row][col] == '~':
            self.board[row][col] = '*' 
            return False
        else:
            return False


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
    
    
    def validate_guess(self):
        """
        function to validate a player's input
        """
        while True:
            try:
                print("guess a row: predict a number between 1 - 5")
                guess_row = int(input("row number:\n")) - 1
                print("guess a column: predict a number between 1 - 5")
                guess_column = int(input("column number:\n")) - 1
                
                if 0 <= guess_row < size and 0 <= guess_column < size:
                    return guess_row, guess_column
                else:
                    print("please enter a number between 1 - 5\n")
            except ValueError:
                print("please enter a number between 1 - 5\n")

    def computer_turn(computer_has_guessed):
        """
        function for the computer to guess
        """
        while True:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            if (row, col) not in computer_has_guessed:
                computer_has_guessed.add((row, col))
                return row, col


    def play_battleships(self, comp_board):
        """
        function to make a move
        """

        player_has_guessed = set()
        computer_has_guessed = set()

        while player_board.hits < player_board.num_ships and comp_board.hits < comp_board.num_ships:
            print(f"{player_name}'s turn: \n")
            guess_row, guess_column = self.validate_guess()


            if (guess_row, guess_column) in player_has_guessed:
                print("you've already guessed that!\n")
            else:
                player_has_guessed.add((guess_row, guess_column))
                if comp_board.get_guess(guess_row, guess_column):
                    print("HIT!")
                else:
                    print("MISS!")

        player_board.print_board(hide_ships=False)
        comp_board.print_board(hide_ships=True)

        if comp_board.hits == comp_board.num_ships:
            print(f"congrtulations {player_name}, you've sunk all my battleships!")
            return 

        comp_row, comp_col = self.computer_turn(computer_has_guessed, comp_board)
        print(f"computer has guessed row {comp_row} and column {comp_col}")

        if player_board.receive_guess(comp_row, comp_col):
            print("Computer HIT your ship!")
        else:
            print("Computer missed.")

        player_board.print_board(hide_ships=False)
        comp_board.print_board(hide_ships=True)

        if player_board.hits == player_board.num_ships:
            print("Game over! The computer has sunk all your ships!")
            return


size = 5
num_ships = 3


player_board = Board(size, num_ships, "Player")
comp_board = Board(size, num_ships, "Computer")


player_game = Play(player_board)
comp_game = Play(comp_board)


player_name = name_and_rules()

player_game.add_ships()
comp_game.add_ships()


player_game.play_battleships(comp_board)




