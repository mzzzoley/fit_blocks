import copy

from src.board import Board
from src.constants import *
from src.piece import Piece
from src.placement import Placement


class FitBlocks:

    def __init__(self, month: int = None, day: int = None, board: list[list] = None, pieces: list[Piece] = None):
        self.board = Board(month, day) if board is None else Board(board=board)
        self.pieces = pieces if pieces else [Piece(five_gun),
                                             Piece(five_l),
                                             Piece(five_z),
                                             Piece(five_bag),
                                             Piece(six_lego),
                                             Piece(five_corner),
                                             Piece(five_factory),
                                             Piece(five_lightning)]
        self.piece_count = len(self.pieces)
        self.placed_pieces = []
        self.attempts_log = []

    def solve(self, print_board: bool = True, find_all: bool = False):
        repeated = 0
        solutions = []
        while self.pieces:
            if repeated > len(self.pieces) and self.pieces:
                if not len(self.placed_pieces):
                    break
                self.take_step_back()
                repeated = 0
            piece = self.pieces.pop()
            result, placement = self.place_piece(piece)
            if result == 'ok':
                self.placed_pieces.append(piece)
                repeated = 0
                self.attempts_log.append([len(self.placed_pieces), placement])
            else:
                self.pieces.insert(0, piece)
                repeated += 1

            if find_all and not self.pieces:
                for solution in solutions:
                    if self.board == solution:
                        break
                solutions.append(copy.deepcopy(self.board))
                self.take_step_back()

        if find_all:
            if print_board:
                print(len(solutions), ' solution(s) found')
                for solution in solutions:
                    print(solution, '\n')
            else:
                return len(solutions)
        else:
            self.output_if_find_one(print_board)

    def place_piece(self, piece: Piece):
        from_row, from_col = self.board.get_next_empty_cell()
        for shape_id, shape in enumerate(piece.shape_list):
            planned_placement = Placement(self.board.board[:], piece, shape_id, from_row, from_col)
            if self.tried_already(planned_placement):
                continue
            if self.board.fit_shape(shape, piece.size, from_row, from_col):
                return 'ok', planned_placement
        else:
            return 'fail', None

    def tried_already(self, new_attempt: Placement):
        for attempt in self.attempts_log:
            if attempt[1] == new_attempt:
                return True

    def take_step_back(self):
        if self.placed_pieces:
            last_tried = self.placed_pieces.pop()
            self.pieces.insert(0, last_tried)
            self.board.pick_up_last_piece()
            while self.attempts_log[-1][0] > len(self.placed_pieces) + 1:
                self.attempts_log.pop()

    def output_if_find_one(self, print_board: bool):
        if len(self.placed_pieces) != self.piece_count:
            print("FAIL")
            return 0
        else:
            if print_board:
                print("SUCCESS")
                print(self.board, '\n')
            return 1
