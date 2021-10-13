"""
Libraries
"""

import re
import random

"""
Legend
~ = co-ordiante doesn't hold ship/ hasn't been guessed
X = co-ordinate holds a ship
+ = co-ordinate holds a ship that has been attacked
- = co-ordinate that was gussesd and resulted in miss
"""


def welcome_message():
    """
    Holds the print statments used in the welcome message,
    displayed each time a new game begins.
    """
    print('WELCOME TO BATTLESHIPS!')
    print('THE BOARD IS A GRID OF 10x10 WITH FOUR SHIPS TO SINK')
    print('AIRCRAFT CARRIER - BATTLECRUISER - SUBMARINE - FRIGATE')
    print('A TOTAL SCORE OF 15 IS REQUIRED TO WIN, 1 POINT PER HIT\n')
    print('NAME CAN BE 10 CHARACTERS MAX. LETTERS, NUMBERS & UNDERSCORES ONLY')


def validate_team_name(name):
    """
    Validates the input name is letters, numbers and underscores only.
    Ensures no longer than 10 characters.
    """

    if not re.match('^[A-Za-z0-9_]*$', name):
        print('INVALID NAME. LETTERS, NUMBERS AND UNDERSCORES ONLY')
        return False
    elif len(name) > 10:
        print('INVALID NAME. 10 CHARACTERS MAX')
        return False
    else:
        return True


def name_input():
    """
    Collects the user name input,
    places it in a variable to use later.
    """
    while True:
        player_name = input('PLEASE ENTER A TEAM NAME:\n')
        if validate_team_name(player_name):
            break
    print(f'\nTHE NAME YOU CHOSE IS: {player_name}\n')
    return player_name


class GameBoard:
    """
    Each board holds the respective players ships,
    the computers ship location will not be on display.
    The relevant board is populated with the opposing
    players guess, marked to indicate if it was a hit or miss.
    """

    # Converts letters for display purposes to numbers for functionailty

    letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

    def __init__(self, name, user):
        self.board = [['~'] * 10 for x in range(10)]
        self.lives = 15
        self.name = name
        self.user = user

    def print_board(self):
        """
         Prints the required board to the terminal.
        """
        print(f'{self.name} BOARD:\n')
        print('  A B C D E F G H I J ')
        print('  -------------------')
        row_number = 0
        for row in self.board:
            print('%d|%s ' % (row_number, ' '.join(row)))
            row_number += 1
        print(f'\nLIVES: {self.lives}\n')

    def check_ship_fits(self, ship_length, row, column, orientation):
        """
        Holds the logic to check if the placed ship fits.
        """
        if orientation == 'H':
            if column + ship_length > 9:
                if self.user == 'player':
                    print('SHIP DOES NOT FIT, TRY AGAIN!\n')
                    return False
                else:
                    return False
            else:
                return True
        else:
            if row + ship_length > 9:
                if self.user == 'player':
                    print('SHIP DOES NOT FIT, TRY AGAIN!\n')
                    return False
                else:
                    return False
            else:
                return True

    def collision_check(self, board, row, column, orientation, ship_length):
        """
        Holds the logic to check for ship collisions upon placement.
        """
        if orientation == 'H':
            for i in range(column, column + ship_length):
                if board[row][i] == 'X':
                    if self.user == 'player':
                        print('YOU HAVE ALREADY PLACED A SHIP IN THESE CO-ORDINATES, TRY AGAIN!\n')
                        return True
                    else:
                        return True
        else:
            for i in range(row, row + ship_length):
                if board[i][column] == 'X':
                    if self.user == 'player':
                        print('YOU HAVE ALREADY PLACED A SHIP IN THESE CO-ORDINATES, TRY AGAIN!\n')
                        return True
                    else:
                        return True
        return False

    def ship_prompt(self, ship_length):
        """
        Prints out to the user which ship they are placing.
        """
        print('THE SAME POINT CANNOT BE USED TWICE, HORIZONTAL AND VERTICAL PLACEMENT ONLY')

        if ship_length == 6:
            print('PLEASE PLACE THE AIRCRAFT CARRIER (1x6)\n')
        elif ship_length == 4:
            print('PLEASE PLACE THE BATTLECRUISER (1x4)\n')
        elif ship_length == 3:
            print('PLEASE PLACE THE SUBMARINE (1x3)\n')
        elif ship_length == 2:
            print('PLEASE PLACE THE FRIGATE (1x2)\n')

    def ship_input(self):
        """
        Collects the users desired:
        orientation, row, column.
        Then used to place the ship on their board.
        """

        while True:
            try:
                orientation = input('ENTER ORIENTATION (H OR V): ').upper()
                if orientation == 'H' or orientation == 'V':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('PLEASE ENTER A VALID ORIENTATION')
        while True:
            try:
                input_column = input('ENTER DESIRED COLUMN (A-J): ').upper()
                if input_column in 'ABCDEFGHIJ':
                    column = self.letters_to_numbers[input_column]
                    break
                else:
                    raise ValueError
            except ValueError:
                print('PLEASE ENTER A VALID LETTER BETWEEN A-J')
        while True:
            try:
                row = input('ENTER DESIRED ROW (0-9): ')
                if row in '0123456789':
                    row = int(row)
                    break
                else:
                    raise ValueError
            except ValueError:
                print('PLEASE ENTER A VALID NUMBER BETWEEN 0-9')

        return orientation, column, row

    def place_ships(self):
        """
        Places the ships randomly on the computers board,
        allows for the player to place their own ships.
        Also Checks the ship fits with no collisions.
        """
        length_of_ships = [6, 4, 3, 2]

        for ship_length in length_of_ships:

            while True:
                if self.user == 'computer':
                    orientation = random.choice(['H', 'V'])
                    row = random.randint(0, 9)
                    column = random.randint(0, 9)
                    if self.check_ship_fits(ship_length, row, column, orientation):
                        if self.collision_check(self.board, row, column, orientation, ship_length) is False:
                            if orientation == 'H':
                                for i in range(column, column + ship_length):
                                    self.board[row][i] = 'X'
                            else:
                                for i in range(row, row + ship_length):
                                    self.board[i][column] = 'X'
                            break
                else:
                    if self.user == 'player':
                        self.ship_prompt(ship_length)
                        orientation, column, row = self.ship_input()
                        if self.check_ship_fits(ship_length, row, column, orientation):
                            if self.collision_check(self.board, row, column, orientation, ship_length) is False:
                                if orientation == 'H':
                                    for i in range(column, column + ship_length):
                                        self.board[row][i] = 'X'
                                else:
                                    for i in range(row, row + ship_length):
                                        self.board[i][column] = 'X'
                                print(' ')
                                self.print_board()
                                break

    def attack_input(self):
        """
        Allows the player to input their desired
        attack co-ordinates. Randomly generates
        the computers co-ordinates.
        """
        while self.lives > 0:
            while True:
                if self.user == 'player':
                    print("ITS YOUR TURN TO ATTACK!\n")
                    try:
                        input_column = input('ENTER DESIRED COLUMN (A-J): ').upper()
                        if input_column in 'ABCDEFGHIJ':
                            column = self.letters_to_numbers[input_column]
                            print(column)  # test
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print('PLEASE ENTER A VALID LETTER BETWEEN A-J')
                elif self.user == 'computer':
                    column = random.randint(0, 9)
                    print(column)  # test
            while True:
                if self.user == 'player':
                    try:
                        row = input('ENTER DESIRED ROW (0-9): ')
                        if row in '0123456789':
                            row = int(row)
                            print(row)  # test
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print('PLEASE ENTER A VALID NUMBER BETWEEN 0-9')
                elif self.user == 'computer':
                    row = random.randint(0, 9)
                    print(row)  # test
            break  # might be in wrong place
        else:
            print('OUT OF LIVES')  # complete later

        return column, row

    def lives_counter(self):
        """
        Updates the lives of the respective player,
        runs each time an attack is completed.
        """
        for row in self.board:
            for column in row:
                if column == '+':
                    self.lives -= 1
        return self.lives


def run_game():
    """
    Starts a new game.
    """
    welcome_message()
    player_name = name_input()
    player_board = GameBoard(player_name, 'player')
    computer_board = GameBoard("COMPUTER's", 'computer')
    player_board.print_board()
    computer_board.print_board()
    computer_board.place_ships()
    computer_board.print_board()  # remove later
    player_board.place_ships()


run_game()
