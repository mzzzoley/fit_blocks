from src.app import FitBlocks


if __name__ == '__main__':
    month = 11
    day = 22
    print(month, '.', day)
    app = FitBlocks(month, day)
    app.solve(find_all=True)


