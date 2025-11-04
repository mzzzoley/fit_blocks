from src.piece import Piece
from dataclasses import dataclass

@dataclass
class Placement:
    board: list[list[list]]
    piece: Piece
    shape: int
    from_row: int
    from_col: int
