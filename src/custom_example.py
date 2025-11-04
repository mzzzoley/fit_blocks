from src.app import FitBlocks
from src.piece import Piece


if __name__ == '__main__':

    my_board = [[0,0,1,1,1],
                [1,0,0,0,0],
                [0,0,0,0,0]]

    piece_p = [[1,1,1,1],
               [1,1,0,0]]

    piece_l = [[1,1,1]]

    piece_d = [[1,1]]

    app = FitBlocks(board=my_board,
                    pieces=[Piece(piece_p),
                            Piece(piece_l),
                            Piece(piece_d)])
    app.solve()