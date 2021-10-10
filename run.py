# Libraries

import re


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


class GameBoard:
    """
    Each board holds the respective players ships,
    the computers ship location will not be on display.
    The relevant board is populated with the opposing
    players guess, marked to indicate if it was a hit or miss.
    """

    def __init__(self, board):
        self.board = board
    
    def print_board(self):
        """
         Prints the board to the terminal
        """
        print('   A B C D E F G H I J ')
        print('   -------------------')
        row_number = 0
        for row in self.board:
            print('%d|%s~' % (row_number, '~'.join(row)))
            row_number += 1


def run_game():
    """
    Starts a new game.
    """
    print('WELCOME TO BATTLESHIPS!')
    print('THE BOARD IS A GRID OF 10X10 WITH FOUR SHIPS TO SINK')
    print('AIRCRAFT CARRIER - BATTLECRUISER - SUBMARINE - FRIGATE')
    print('A TOTAL SCORE OF 15 IS REQUIRED TO WIN, 1 POINT PER HIT\n')
    print('NAME CAN BE 10 CHARACTERS MAX. LETTERS, NUMBERS & UNDERSCORES ONLY')
    while True:
        player_name = input('PLEASE ENTER A TEAM NAME:\n')
        if validate_team_name(player_name):
            break
    print(f'\nTHE NAME YOU CHOSE IS: {player_name}\n')
    player_board = GameBoard([[' '] * 10 for x in range(10)])
    GameBoard.print_board(player_board)


run_game()
