import itertools


class Board:

    def __init__(self, month: int, day: int):
        self.month = month
        self.day = day
        self.board = self.create_board()
        self.board_size = self.get_board_size()
        self.placed_piece_cnt = 0
        self.board_history = []

    def __str__(self):
        text = ''
        text += '\n'.join(str(r) for r in self.board) + '\n'
        return text[:-1] if text else ''

    def create_board(self):
        board = [[0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1]]
        if self.month < 7:
            board[0][self.month - 1] = 1
        else:
            board[1][self.month % 7] = 1
        board[self.day // 7 + 2][self.day % 7 - 1] = 1
        return board

    def get_board_size(self):
        return sum(map(sum, zip(*self.board)))

    def fit_shape(self, piece, size: int, from_row: int, from_col: int):
        new = []
        if 0 < from_row:
            new += self.board[:from_row]
        try:
            for row, piece_row in enumerate(piece):
                new_board_row_id = from_row + row
                if new_board_row_id > len(self.board) - 1:
                    raise StopIteration
                if sum(piece_row) > 0 and len(self.board) < row + 1:
                        raise StopIteration
                elif len(self.board) < row + 1:
                    continue
                if sum(piece_row) == 0:
                    new.append(self.board[new_board_row_id])
                    if sum(map(sum, zip(*piece[row:]))) == 0 and len(new) == len(self.board):
                        break
                    continue
                board_row = self.board[new_board_row_id]
                new.append([])
                new_board_col_from = min(len(self.board[new_board_row_id]) - len(piece_row), from_col)
                if from_col:
                    new[new_board_row_id] += board_row[:new_board_col_from]
                for col, combined in enumerate(itertools.zip_longest(board_row[new_board_col_from:],
                                                                     piece_row[:],
                                                                     fillvalue=0)):
                    if combined.count(0) == 0:
                        raise StopIteration
                    new[new_board_row_id] += [self.addval(combined)]
                    if len(new[new_board_row_id]) > len(self.board[new_board_row_id]):
                        raise StopIteration

            if (rows_missing := len(self.board) - len(new)) > 0:
                new += (self.board[-rows_missing:])
            self.board_history.append(self.board[:])
            self.board = new[:]
            self.board_size += size
            self.placed_piece_cnt += 1
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
                    return row_id, col_id

    def pick_up_last_piece(self):
        self.board = self.board_history.pop()
        self.board_size = self.get_board_size()
        self.placed_piece_cnt -= 1
