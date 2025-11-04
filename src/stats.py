from src.__main__ import FitBlocks
from timer import timeit

@timeit
def stats():
    cnt = 0
    success = 0
    for m in range(1, 13):
        for d in range(1, 32):
            cnt += 1
            print(m, d, sep='.')
            app = FitBlocks(m, d)
            success += app.solve(print_board=False)
    print(success, ' found out of ', cnt)

if __name__ == '__main__':
    stats()