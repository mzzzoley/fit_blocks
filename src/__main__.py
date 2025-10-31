import itertools

from constants import *
from piece import Piece


class Board:

    def __init__(self):
        self.board = [[0,0,0,0],
                      [0,0,1,0],
                      [0,0,0,0]]
        self.board_size = sum(map(sum, zip(*self.board)))
        self.placed_piece_cnt = 0

    def __str__(self):
        text = ''
        text += '\n'.join(str(r) for r in self.board) + '\n'
        return text[:-1] if text else ''

    def place_piece(self, piece:Piece):
        """
            Fit piece on board
            Return True if fits
        """
        for from_row, from_col in self.get_next_empty_cell():
            print(from_row, from_col)
            for shape in piece:
                print('piece', shape)
                if self.fit_shape(shape, piece.size, from_row, from_col):
                    return 1
        return 0

    def fit_shape(self, piece, size: int, from_row: int, from_col: int):

        new = []
        if 0 < from_row:
            new += self.board[:from_row]
        try:
            for row, piece_row in enumerate(piece):
                # if piece is smaller than board, 2x2 piece in 1/1 place in 4x4 board, last two rows will be omitted
                new_board_row_id = from_row + row
                if sum(piece_row) > 0 and len(self.board) < row + 1:
                        raise StopIteration
                elif len(self.board) < row + 1:
                    continue
                if sum(piece_row) == 0:
                    new.append(self.board[new_board_row_id])
                    continue
                board_row = self.board[new_board_row_id]
                new.append([])
                print('board_row', board_row, 'piece_row', piece_row)

                new_board_col_from = min(len(self.board[new_board_row_id]) - len(piece_row), from_col)
                if from_col:
                    new[new_board_row_id] += board_row[:new_board_col_from]
                for col, combined in enumerate(itertools.zip_longest(board_row[new_board_col_from:],
                                                                     piece_row[:],
                                                                     fillvalue=0)):
                    if combined.count(0) < 1:
                        raise StopIteration
                    new[new_board_row_id] += [self.addval(combined)]
                    if len(new[new_board_row_id]) > len(self.board[new_board_row_id]):
                        raise StopIteration
                    print(new)
            else:
                self.board = new[:]
                self.board_size += size
                self.placed_piece_cnt += 1
                print('new board', self.board)
                return True
        except StopIteration:
            pass

    def addval(self, combined):
        if sum(combined) == 0:
            return 0
        elif combined[0]:
            return combined[0]
        else:
            return self.placed_piece_cnt + 2

    def get_next_empty_cell(self):
        for row_id, row in enumerate(self.board):
            for col_id, cell in enumerate(row):
                if cell == 0:
                    yield row_id, col_id


class FitBlocks:

    def __init__(self):
        self.board = Board()
        # self.pieces = [Piece(six_lego),
        #                Piece(five_bag)]
        # self.pieces = [Piece(five_bag),
        #                Piece(six_lego)]
        # self.pieces = [Piece(five_gun),
        #                Piece(three_corner),
        #                Piece(three_corner)]
        self.pieces = [Piece(three_corner),
                       Piece(five_gun),
                       Piece(three_corner)]
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
            if repeated == len(self.pieces):
                if self.placed_pieces:
                    last_tried = self.placed_pieces.pop()
                    self.pieces.insert(0, last_tried)
                break

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
