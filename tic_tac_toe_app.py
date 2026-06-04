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

    def get_cell(self, x, y):
        cell_index = y * self.width + x
        return self.cells[cell_index]
    
    def get_num_open_cells(self):
        num_open_cells = 0
        for cell in self.cells:
            if cell == -1:
                num_open_cells += 1

    def reset_board(self):
        for c in range(len(self.cells)):
            self.cells[c] = -1

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

    def evaluate_game(self):
        if self.board == None:
            return 0
        
        #check rows
        for i in range(self.board.height):
            if self.board.get_cell(0, i) == self.board.get_cell(1, i) and self.board.get_cell(1, i) == self.board.get_cell(2, i):
                if self.board.get_cell(0, i) == 1:
                    return 2 #O wins!
                elif self.board.get_cell(0, i) == 0:
                    return 1 #X wins!
                
        #check columns
        for i in range(self.board.width):
            if self.board.get_cell(i, 0) == self.board.get_cell(i, 1) and self.board.get_cell(i, 1) == self.board.get_cell(i, 2):
                if self.board.get_cell(i, 0) == 1:
                    return 2 #O wins!
                elif self.board.get_cell(i, 0) == 0:
                    return 1 #X wins!
        
        #check diagonals
        if self.board.get_cell(0, 0) == self.board.get_cell(1, 1) and self.board.get_cell(1, 1) == self.board.get_cell(2, 2):
            if self.board.get_cell(0, 0) == 1:
                return 2 #O wins!
            elif self.board.get_cell(0, 0) == 0:
                return 1 #X wins!
            
        #check diagonals
        if self.board.get_cell(2, 0) == self.board.get_cell(1, 1) and self.board.get_cell(1, 1) == self.board.get_cell(2, 0):
            if self.board.get_cell(2, 0) == 1:
                return 2 #O wins!
            elif self.board.get_cell(2, 0) == 0:
                return 1 #X wins!
            
        if self.board.get_num_open_cells() == 0:
            return 0 #TIE!
        
        return -1 #Game is still going!

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
        self.game.board.set_cell(self.get_random_move(), 0)

        rendered_board = self.game.board.render()

        game_result = self.game.evaluate_game()

        if game_result == -1:
            return rendered_board
        elif game_result == 0:
            result = f"Draw\n\n{rendered_board}"
            self.game.board.reset_board()

            return result
        elif game_result == 1:
            result = f"X won!\n\n{rendered_board}"
            self.game.board.reset_board()

            return result
        elif game_result == 2:
            result = f"O won!\n\n{rendered_board}"
            self.game.board.reset_board()

            return result



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