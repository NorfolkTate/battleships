import random


class Board:
    """
    class for the game boards
    """

    def __init__(self, size, num_ships, board_type):
        self.size = size
        self.board = [["~" for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.hits = 0
        self.type = board_type

    def print_board(self, hide_ships = False):
        """
        function to print the boards to the terminal
        rows and columns start at 1 for a more user friendly experience
        """
        print(f"{self.type} Board:")        
        print("  " + " ".join(str(x) for x in range(1, self.size + 1)))
        for row_number, row in enumerate(self.board, start=1):
            display_row = ['~' if hide_ships and cell == 'O' else cell for cell in row]
            print(f"{row_number} {' '.join(display_row)}")
        print()

    def get_guess(self, row, column):
        """
        function to get and process a guess
        """
        if self.board[row][column] == 'O':
            self.board[row][column] = 'X' 
            self.hits += 1
            return True
        elif self.board[row][column] == '~':
            self.board[row][column] = '*' 
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
    print("Guess a row between 1 - 5\n")
    print("Guess a column between 1 - 5\n")

    print(f"Let's play battleships, {player_name}, good luck!")
    return player_name



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
            column = random.randint(0, size - 1)
        
            if self.board.board[row][column] == '~':
                self.board.board[row][column] = 'O'
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
                
                if 0 <= guess_row < self.board.size and 0 <= guess_column < self.board.size:
                    return guess_row, guess_column
                else:
                    print("please enter a number between 1 - 5\n")
            except ValueError:
                print("please enter a number between 1 - 5\n")

    def computer_turn(self, computer_has_guessed):
        """
        Function for the computer to guess.
        """
        while True:
            computer_row = random.randint(0, self.board.size - 1)
            computer_column = random.randint(0, self.board.size - 1)
            if (computer_row, computer_column) not in computer_has_guessed:
                computer_has_guessed.add((computer_row, computer_column))
                return computer_row, computer_column



    def play_battleships(self, computer_board):
        """
        Function to play the game.
        """
        player_has_guessed = set()
        computer_has_guessed = set()

        while self.board.hits < self.board.num_ships and computer_board.hits < computer_board.num_ships:
            print(f"{player_name}'s turn: \n")
            guess_row, guess_column = self.validate_guess()

            if (guess_row, guess_column) in player_has_guessed:
                print("You've already guessed that!\n")
            else:
                player_has_guessed.add((guess_row, guess_column))
                if computer_board.get_guess(guess_row, guess_column):
                    print("HIT!")
                else:
                    print("MISS!")

            self.board.print_board(hide_ships=False)
            computer_board.print_board(hide_ships=True)

            if computer_board.hits == computer_board.num_ships:
                print(f"Congratulations {player_name}, you've sunk all the computer's battleships!")
                return

            print("Computer's turn:")
            computer_row, computer_column = self.computer_turn(computer_has_guessed)
            print(f"Computer has guessed row {computer_row + 1} and column {computer_column + 1}")

            if self.board.get_guess(computer_row, computer_column):
                print("Computer HIT your ship!")
            else:
                print("Computer missed.")

            self.board.print_board(hide_ships=False)
            computer_board.print_board(hide_ships=True)

            if self.board.hits == self.board.num_ships:
                print("Game over! The computer has sunk all your ships!")
                return

size = 5
num_ships = 3

player_board = Board(size, num_ships, "Player")
computer_board = Board(size, num_ships, "Computer")

player_name = name_and_rules()

player_game = Play(player_board)
computer_game = Play(computer_board)

player_game.add_ships()
computer_game.add_ships()

player_board.print_board(hide_ships=False)
computer_board.print_board(hide_ships=True)

player_game.play_battleships(computer_board)




