import os
import sys

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
        for combo in [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]:
            result = True

            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False

            if result == True:
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

    def ai_move(self, player):

        if player == "X":
            enemy = "O"
        if player == "O":
            enemy = "X"

        if(self.cells[5] == " "):
            self.update_cell(5, player)
            return

        for i in range(1,10):
            if self.cells[i] == " ":
                self.update_cell(i, player)
                break

board = Board()

def print_header():
    print("Welcome to Tic Tac Toe Game \n")

def refrash_screan():
    os.system("clear")
    print_header()
    board.display()

two_players = raw_input("Would you like to play two players? (Y/N) > ").upper()

if two_players != "Y" and two_players != "N":
    two_players = raw_input("Please select Y or N ! > ").upper()

if two_players != "Y" and two_players != "N":
    sys.exit("\n Your chose isn't corect! Please run game again :) \n")

if two_players == "Y":
    while True:
        refrash_screan()

        # Player X functionality
        x_choice = int(raw_input("\n X) Please choose 1-9. > "))
        board.update_cell(x_choice, "X")
        refrash_screan()
        if board.is_winner("X"):
            print("\n Player X wins! \n")
            play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
            if play_again == "Y":
                board.reset()
                continue
            else:
                break

        if board.is_tie():
            print("\n Game ends with tie! \n")
            play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
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
            play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
            if play_again == "Y":
                board.reset()
                continue
            else:
                break

        if board.is_tie():
            print("\n Game ends with tie! \n")
            play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
            if play_again == "Y":
                board.reset()
                continue
            else:
                break
else:
    chose_player = raw_input("Would you like to play with X or O ? (X/O) > ").upper()
    if chose_player != "X" and chose_player != "O":
        chose_player = raw_input("Please select X or O ! > ").upper()

    if chose_player != "X" and chose_player != "O":
        sys.exit("\n Your chose isn't corect! Please run game again :) \n")

    if chose_player == "X":
        machine = "O"

        while True:
            refrash_screan()

            # Player X functionality
            x_choice = int(raw_input("\n X) Please choose 1-9. > "))
            board.update_cell(x_choice, chose_player)
            refrash_screan()
            if board.is_winner(chose_player):
                print("\n Player X wins! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break

            if board.is_tie():
                print("\n Game ends with tie! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break

            # Ai Player functionality
            board.ai_move(machine)
            refrash_screan()
            if board.is_winner(machine):
                print("\n Player O wins! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break

            if board.is_tie():
                print("\n Game ends with tie! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break

    else:
        machine = "X"
        while True:
            refrash_screan()

            # Ai Player functionality
            board.ai_move(machine)
            refrash_screan()
            if board.is_winner(machine):
                print("\n Player X wins! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break

            if board.is_tie():
                print("\n Game ends with tie! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break

            # Player O functionality
            x_choice = int(raw_input("\n O) Please choose 1-9. > "))
            board.update_cell(x_choice, chose_player)
            refrash_screan()
            if board.is_winner(chose_player):
                print("\n Player O wins! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break

            if board.is_tie():
                print("\n Game ends with tie! \n")
                play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    board.reset()
                    continue
                else:
                    break
