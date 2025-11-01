import itertools

from piece import Piece


class Board:

    def __init__(self):
        self.board = [[0,0,0,0],
                      [0,0,1,0],
                      [0,0,0,0]]
        self.board_size = self.get_board_size()
        self.placed_piece_cnt = 0
        self.board_history = []

    def __str__(self):
        text = ''
        text += '\n'.join(str(r) for r in self.board) + '\n'
        return text[:-1] if text else ''

    def get_board_size(self):
        return sum(map(sum, zip(*self.board)))

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
                if new_board_row_id > len(self.board) - 1:
                    raise StopIteration
                if sum(piece_row) > 0 and len(self.board) < row + 1:
                        raise StopIteration
                elif len(self.board) < row + 1:
                    continue
                if sum(piece_row) == 0:
                    new.append(self.board[new_board_row_id])
                    continue
                board_row = self.board[new_board_row_id]
                new.append([])
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
            else:
                if (rows_missing := len(self.board) - len(new)) > 0:
                    new += (self.board[-rows_missing:])
                self.board = new[:]
                self.board_size += size
                self.placed_piece_cnt += 1
                self.board_history.append(self.board)
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

    def pick_up_last_piece(self):
        self.board = self.board_history.pop()
        self.board_size = self.get_board_size()
        self.placed_piece_cnt -= 1
