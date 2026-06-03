import random

from base_bot_app import BaseBotApp

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.cells = []

        for x in range(width):
            for y in range(height):
                self.cells.append(-1)
    
    def render(self):
        return f""" {self.get_cell_display(self.cells[0])} | {self.get_cell_display(self.cells[1])} | {self.get_cell_display(self.cells[2])}
 _   _   _
 {self.get_cell_display(self.cells[3])} | {self.get_cell_display(self.cells[4])} | {self.get_cell_display(self.cells[5])}
 _   _   _
 {self.get_cell_display(self.cells[6])} | {self.get_cell_display(self.cells[7])} | {self.get_cell_display(self.cells[8])}
"""
    def set_cell(self, index, value):
        self.cells[index] = value

    def get_cell_display(self, cell):
        if cell == -1:
            return ' '
        elif cell == 0:
            return 'X'
        else:
            return 'O'
        


class TicTacToeGame:
    def __init__(self, board : Board):
        self.board : Board = board
        


class TicTacToeApp(BaseBotApp):
    name = "Tic Tac Toe"
    description = "Play tic tac toe against a bot"

    game : TicTacToeGame = TicTacToeGame(Board(3, 3))

    def register_commands(self):
        self.add_command(
            "take_space",
            self.player_make_move,
            'Make a move for the game, example: take_space "1"'
        )

    def player_make_move(self, args, options):
        if len(args) < 1:
            return "Not enough arguments"
       
        #Player Move
        cell_number = int(args[0])
        self.game.board.set_cell(cell_number, 1)

        #Bot Move
        self.game.board.set_cell(self.get_random_move, 0)

        rendered_board = self.game.board.render()
        return rendered_board



    def get_random_move(self):
        random_number = random.randrange(0, 9)
        while self.game.board.cells[random_number] != -1:
            random_number = random.randrange(0, 9)
        
        return random_number
        



########################### TEST CODE ###########################
# board = Board(3, 3)
# board.set_cell(0, 0)
# board.set_cell(4, 1)

# print(board.render())