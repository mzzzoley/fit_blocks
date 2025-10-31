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
            for form in piece:
                print('piece', form)
                if self.__fit_form(form, piece.size, from_row, from_col):
                    return

    def __fit_form(self, piece, size: int, from_row: int, from_col: int):

        new = []
        if 0 < from_row:
            new += self.board[:from_row]
        try:
            for row, piece_row in enumerate(piece):
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
                if from_col:
                    new[new_board_row_id] += board_row[:from_col]
                for col, combined in enumerate(itertools.zip_longest(board_row[max(from_col-1, 0):],
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
    # def __fit_form(self, piece, size: int, from_row: int, from_col: int):
    #
    #     new = []
    #     row = 0
    #     try:
    #         for board_row, piece_row in zip(self.board[:], piece[:]):
    #              # from_row, from_col is already provided in outer loop
    #              # then here we loop again, that is the problem
    #             new.append([])
    #             print('board_row', board_row, 'piece_row', piece_row)
    #             if row < from_row and new[row] != self.board[row]:
    #                 new[row] += self.board[row]
    #                 row += 1
    #                 continue
    #             for col, combined in enumerate(zip(board_row[:], piece_row)):
    #                 if col < from_col and new[row] != self.board[row]:
    #                     new[row] += [board_row[col]]
    #                     continue
    #                 if (cell := sum(combined)) > self.placed_piece_cnt + 1:
    #                     raise StopIteration
    #                 new[row] += [cell]
    #                 print(new)
    #             row += 1
    #         else:
    #             if size == sum(map(sum, zip(*new))) - sum(map(sum, zip(*self.board))):  # every cell fits
    #                 self.board = new[:]
    #                 self.board_size += size
    #                 self.placed_piece_cnt += 1
    #                 return True
    #     except StopIteration:
    #         pass

    def get_next_empty_cell(self):
        for row_id, row in enumerate(self.board):
            for col_id, cell in enumerate(row):
                if cell == 0:
                    yield row_id, col_id


class FitBlocks:

    def __init__(self):
        self.board = Board()
        self.pieces = [Piece(five_gun),
                       Piece(three_corner),
                       Piece(three_corner)]

    def solve(self):
        for piece in self.pieces:
            self.board.place_piece(piece)
            print(self.board)


if __name__ == '__main__':
    app = FitBlocks()
    app.solve()

    # piece_four = [[1,1],
    #               [1,1]]
    # piece_two = [[0,0],
    #              [1,1]]
    #
    # four = Piece(piece_four)
    # two = Piece(piece_two)
    # two_two = Piece(piece_two)

    # pipi = [[1,0,0,0],
    #         [1,0,0,0],
    #         [1,1,0,0],
    #         [1,0,0,0]]
    #
    # pi = Piece(pipi)
    # print(pi)


    # board = [[0,0],
    #          [0,0],
    #          [1,0]]
    #
    # piece = [[1,0],
    #          [1,0],
    #          [1,0]]
