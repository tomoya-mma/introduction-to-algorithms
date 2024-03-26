import enum
import sys


class Direction(enum.Enum):

    UP = 'up'
    LEFT = 'left'
    DIAGONAL = 'diagonal'


def lcs_length(x, y):
    results = [[-sys.maxsize for _ in range(max(len(x), len(y)))]
               for _ in range(max(len(x), len(y)))]
    directions = [[None for _ in range(max(len(x), len(y)))]
                  for _ in range(max(len(x), len(y)))]

    for i in range(len(x)):
        for j in range(len(y)):
            if i == 0 and j == 0:
                if x[0] == y[0]:
                    result = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    result = 0
                    directions[i][j] = Direction.DIAGONAL
            elif i == 0:
                if x[0] == y[j]:
                    result = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    result = results[i][j - 1]
                    directions[i][j] = Direction.LEFT
            elif j == 0:
                if x[i] == y[0]:
                    result = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    result = results[i - 1][j]
                    directions[i][j] = Direction.UP
            else:
                if x[i] == y[j]:
                    result = results[i - 1][j - 1] + 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    if results[i - 1][j] < results[i][j - 1]:
                        result = results[i][j - 1]
                        directions[i][j] = Direction.LEFT
                    else:
                        result = results[i - 1][j]
                        directions[i][j] = Direction.UP

            results[i][j] = result

    return results, directions


def print_optimal_strategy(directions, x, i, j):
    if i < 0 or j < 0:
        return
    if directions[i][j] == Direction.DIAGONAL:
        print_optimal_strategy(directions, x, i - 1, j - 1)
        print(x[i], end='')
    elif directions[i][j] == Direction.LEFT:
        print_optimal_strategy(directions, x, i, j - 1)
    else:
        print_optimal_strategy(directions, x, i - 1, j)


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    results, directions = lcs_length(x, y)
    for i, _x in enumerate(x):
        print(f"--- i = {i} ---")
        for j, _y in enumerate(y):
            print(f"i = {i}, j = {j}, x = {x[:i + 1]}, "
                  f"y = {y[:j + 1]} / result = {results[i][j]} ", end='(')
            print_optimal_strategy(directions, x, i, j)
            print(')')
