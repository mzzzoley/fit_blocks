from constants import *
from piece import Piece
from board import Board

class FitBlocks:

    def __init__(self):
        self.board = Board()
        # self.pieces = [Piece(six_lego),
        #                Piece(five_bag)]
        # self.pieces = [Piece(five_bag),
        #                Piece(six_lego)]
        self.pieces = [Piece(five_gun),
                       Piece(three_corner),
                       Piece(three_corner)]
        # self.pieces = [Piece(three_corner),
        #                Piece(three_corner),
        #                Piece(five_gun)]
        # self.pieces = [Piece(three_corner),
        #                Piece(five_gun),
        #                Piece(three_corner)]
        self.piece_count = len(self.pieces)
        self.placed_pieces = []

    def solve(self):
        repeated = 0
        while self.pieces:
            piece = self.pieces.pop()
            if self.board.place_piece(piece):
                self.placed_pieces.append(piece)
                repeated = 0
            else:
                self.pieces.insert(0, piece)
                repeated += 1
            if repeated >= len(self.pieces) and self.pieces:
                if self.placed_pieces:
                    last_tried = self.placed_pieces.pop()
                    self.pieces.insert(0, last_tried)
                    self.board.pick_up_last_piece()
                break
            print('end of while loop', self.board, sep='\n')

        if len(self.placed_pieces) != self.piece_count:
            print("FAIL", "Pieces don't fit", sep='\n')
        else:
            print("SUCCESS")
            print(self.board)

    def place_piece(self, piece:Piece):
        """
            Fit piece on board
            Return True if fits
        """
        for from_row, from_col in self.board.get_next_empty_cell():
            print(from_row, from_col)
            for shape in piece:
                print('piece', shape)
                if self.board.fit_shape(shape, piece.size, from_row, from_col):
                    return True


if __name__ == '__main__':
    app = FitBlocks()
    app.solve()
