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
            if app.solve(print_board=False):
                success += 1
            else:
                print(f'{m}.{d}', ' not found')
    print(success, ' found out of ', cnt)

if __name__ == '__main__':
    stats()