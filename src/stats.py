import pandas as pd
from src.app import FitBlocks
from timer import timeit


@timeit
def stats(print_boards: bool=False):
    cnt = 0
    success = 0
    for m in range(1, 13):
        for d in range(1, 32):
            cnt += 1
            print(m, d, sep='.')
            app = FitBlocks(m, d)
            if app.solve(print_board=print_boards):
                success += 1
            else:
                print(f'{m}.{d}', ' not found')
    print(success, ' found out of ', cnt)

@timeit
def stats_every_solution():
    cnt = 0
    row_list = []

    for m in range(1, 13):
        for d in range(1, 32):
            cnt += 1
            app = FitBlocks(m, d)
            solution_count = app.solve(print_board=False, find_all=True)
            row_list.append({'month':m,
                             'day':d,
                              'solution_count':solution_count})
            print(f'{m}.{d}', f' {solution_count} solutions found')
    result = pd.DataFrame(row_list, columns=('month', 'day', 'solution_count'))
    result.sort_values('solution_count')
    result.to_csv('every_result.csv')


if __name__ == '__main__':
    stats(True)
    # stats()
    # stats_every_solution() # takes over 2 hours to create solution count for every day