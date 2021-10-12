"""
Libraries
"""

import re
import random

# Used to determine board size and populate welcome message

BOARD = [['~'] * 10 for x in range(10)]
SIZE = '10x10'


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
    print(f'THE BOARD IS A GRID OF {SIZE} WITH FOUR SHIPS TO SINK')
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


def check_ship_fits(ship_length, row, column, orientation):
    """
    Holds the logic to check if the placed ship fits.
    """
    if orientation == 'H':
        if column + ship_length > 9:
            return False
        else:
            return True
    else:
        if row + ship_length > 9:
            return False
        else:
            return True


def collision_check(board, row, column, orientation, ship_length):
    """
    Holds the logic to check for ship collisions upon placement.
    """
    if orientation == 'H':
        for i in range(column, column + ship_length):
            if board[row][i] == 'X':
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == 'X':
                return True
    return False


def get_letters_to_numbers():
    """
    Converts the letters used for display to numbers for functional use.
    """
    letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    return letters_to_numbers


def ship_prompt(length_of_ships):
    """
    Prints out to the user which ship they are placing.
    """
    for ship_length in length_of_ships:
        if ship_length == 6:
            print('PLEASE PLACE THE AIRCRAFT CARRIER (1x6)')
        elif ship_length == 4:
            print('PLEASE PLACE THE BATTLECRUISER (1x4)')
        elif ship_length == 3:
            print('PLEASE PLACE THE SUBMARINE (1x3)')
        elif ship_length == 2:
            print('PLEASE PLACE THE FRIGATE (1x2)')


def ship_input(place_ship):
    """
    Collects the users desired:
    orientation, row, column.
    Then used to place the ship on their board.
    """


class GameBoard:
    """
    Each board holds the respective players ships,
    the computers ship location will not be on display.
    The relevant board is populated with the opposing
    players guess, marked to indicate if it was a hit or miss.
    """

    def __init__(self, board, name, score, user):
        self.board = board
        self.name = name
        self.score = score
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
        print(f'\nSCORE: {self.score}\n')

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
                    if check_ship_fits(ship_length, row, column, orientation):
                        if collision_check(self.board, row, column, orientation, ship_length) is False:
                            if orientation == 'H':
                                for i in range(column, column + ship_length):
                                    self.board[row][i] = 'X'
                            else:
                                for i in range(row, row + ship_length):
                                    self.board[i][column] = 'X'
                            break
                else:
                    place_ship = True
                    ship_prompt(length_of_ships)
                    row, column, orientation = ship_input(place_ship)
                    if check_ship_fits(ship_length, row, column, orientation):
                        if collision_check(self.board, row, column, orientation, ship_length) is False:
                            if orientation == 'H':
                                for i in range(column, column + ship_length):
                                    self.board[row][i] = 'X'
                            else:
                                for i in range(row, row + ship_length):
                                    self.board[i][column] = 'X'
                            break


def run_game():
    """
    Starts a new game.
    """
    welcome_message()
    player_name = name_input()
    player_board = GameBoard(BOARD, player_name, 0, 'player')
    computer_board = GameBoard(BOARD, "COMPUTER's", 0, 'computer')
    GameBoard.print_board(player_board)
    GameBoard.print_board(computer_board)
    GameBoard.place_ships(computer_board)


run_game()
