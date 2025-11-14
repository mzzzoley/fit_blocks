import itertools
import calendar

class Board:

    def __init__(self, month: int = None, day: int = None, board: list[list] = None):
        self.month = month if board is None else None
        self.day = day
        self.board = board if board is not None else self.create_board()
        self.board_size = self.get_board_size()
        self.placed_piece_cnt = 0
        self.board_history = []

    def __str__(self):
        if self.month:
            if self.month < 7:
                self.board[0][self.month - 1] = calendar.month_name[self.month][:3]
            else:
                self.board[1][self.month % 7] = calendar.month_name[self.month][:3]
            self.board[(self.day - 1) // 7 + 2][self.day % 7 - 1] = 'Day' + str(self.day)

        text = ' | ' + "-" * (len(self.board[0]) * 8 - 3) + ' |'
        text += '\n'
        for row in self.board:
            text += " | " + " | ".join(f"{str('X' if item == 1 else item).center(5)}" for item in row)  + ' |'
            text += '\n'
            text += " | " + "-" * (len(row) * 8 - 3) + " | "
            text += '\n'
        return text

    def __eq__(self, other):
        return self.board == other.board

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
        board[(self.day - 1) // 7 + 2][self.day % 7 - 1] = 1
        return board

    def get_board_size(self):
        return sum(map(sum, zip(*self.board)))

    def fit_shape(self, piece, size: int, from_row: int, from_col: int):
        new = []
        starter_zeroes_in_piece = 0
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
                if row == 0:
                    for cell in piece_row:
                        if cell == 0:
                            starter_zeroes_in_piece += 1
                        else:
                            break
                new_board_col_from = min(max(len(self.board[new_board_row_id]) - len(piece_row),0),
                                         max(from_col-starter_zeroes_in_piece, 0))
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
