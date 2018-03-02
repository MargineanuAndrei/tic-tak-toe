import os

#Main game board class
class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s "%(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_number, player):
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player

    def is_winner(self, player):
        if(self.cells[1] == player and self.cells[2] == player and self.cells[3] == player):
            return True

        if(self.cells[4] == player and self.cells[5] == player and self.cells[6] == player):
            return True

        if(self.cells[7] == player and self.cells[8] == player and self.cells[9] == player):
            return True

        if(self.cells[1] == player and self.cells[4] == player and self.cells[7] == player):
            return True

        if(self.cells[2] == player and self.cells[5] == player and self.cells[8] == player):
            return True

        if(self.cells[3] == player and self.cells[6] == player and self.cells[9] == player):
            return True

        if(self.cells[1] == player and self.cells[5] == player and self.cells[9] == player):
            return True

        if(self.cells[3] == player and self.cells[5] == player and self.cells[7] == player):
            return True

        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

board = Board()

def print_header():
    print("Welcome to Tic Tac Toe Game \n")

def refrash_screan():
    os.system("clear")
    print_header()
    board.display()

while True:
    refrash_screan()

    # Player X functionality
    x_choice = int(raw_input("\n X) Please choose 1-9. > "))
    board.update_cell(x_choice, "X")
    refrash_screan()
    if board.is_winner("X"):
        print("\n Player X wins! \n")
        play_again = raw_input("Would you like to play again? (Y?N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\n Game ends with tie! \n")
        play_again = raw_input("Would you like to play again? (Y?N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Player O functionality
    o_choice = int(raw_input("\n O) Please choose 1-9. > "))
    board.update_cell(o_choice, "O")
    refrash_screan()
    if board.is_winner("O"):
        print("\n Player O wins! \n")
        play_again = raw_input("Would you like to play again? (Y?N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\n Game ends with tie! \n")
        play_again = raw_input("Would you like to play again? (Y?N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
