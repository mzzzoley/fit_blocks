from src.app import FitBlocks


if __name__ == '__main__':
    month = 10
    day = 6
    print(month, '.', day)
    app = FitBlocks(month, day)
    app.solve()


