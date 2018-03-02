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


board = Board()

def print_header():
    print("Welcome to Tic Tac Toe Game \n")

def refrash_screan():
    os.system("clear")
    print_header()
    board.display()

while True:
    refrash_screan()
    x_choice = int(raw_input("\n X) Please choose 1-9. > "))
    board.update_cell(x_choice, "X")

    refrash_screan()
    o_choice = int(raw_input("\n O) Please choose 1-9. > "))
    board.update_cell(o_choice, "O")
