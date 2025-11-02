from constants import *
from piece import Piece
from board import Board
from dataclasses import dataclass

@dataclass
class Placement:
    board: list[list[list]]
    piece: Piece
    shape: int
    from_row: int
    from_col: int


class FitBlocks:

    def __init__(self, month: int, day: int):
        self.board = Board(month, day)
        self.pieces = [Piece(five_gun),
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

    def solve(self):
        repeated = 0
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
                self.attempts_log.append(placement)
            else:
                self.pieces.insert(0, piece)
                repeated += 1

        if len(self.placed_pieces) != self.piece_count:
            print("FAIL", "Pieces don't fit", sep='\n')
        else:
            print("SUCCESS")
            print(self.board, '\n')

    def place_piece(self, piece: Piece):
        """
            Fit piece on board
            Return True if fits
        """
        from_row, from_col = self.board.get_next_empty_cell()
        for shape_id, shape in enumerate(piece.shape_list):
            planned_placement = Placement(self.board.board_history[:], piece, shape_id, from_row, from_col)
            if self.tried_already(planned_placement):
                continue
            if self.board.fit_shape(shape, piece.size, from_row, from_col):
                return 'ok', planned_placement
        else:
            return 'fail', None

    def tried_already(self, new_attempt: Placement):
        for attempt in self.attempts_log:
            if attempt == new_attempt:
                return True

    def take_step_back(self):
        if self.placed_pieces:
            last_tried = self.placed_pieces.pop()
            self.pieces.insert(0, last_tried)
            self.board.pick_up_last_piece()

if __name__ == '__main__':
    month = 7
    day = 11
    app = FitBlocks(month, day)
    app.solve()
