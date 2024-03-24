import sys


def matrix_chain_order(p):
    results = [[sys.maxsize for _ in range(
        len(p) + 1)] for _ in range(len(p) + 1)]
    slices = [[-1 for _ in range(
        len(p) + 1)] for _ in range(len(p) + 1)]

    for i in range(len(p) - 1):
        results[i][i] = 0

    diff = 1
    while diff < len(p) - 1:
        i, j = 0, diff

        while j < len(p) - 1:
            result = sys.maxsize
            for k in range(i, j):
                if result > results[i][k] + results[k + 1][j] + p[i] * p[k + 1] * p[j + 1]:
                    result = results[i][k] + results[k +
                                                     1][j] + p[i] * p[k + 1] * p[j + 1]
                    slices[i][j] = k

            results[i][j] = result

            i += 1
            j += 1

        diff += 1

    return results, slices


def print_optimal_strategy(slices, i, j):
    if i == j:
        print(f"A{i}", end='')
    else:
        print('(', end='')
        print_optimal_strategy(slices, i, slices[i][j])
        print_optimal_strategy(slices, slices[i][j] + 1, j)
        print(')', end='')


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]

    print("  i |", end='')
    for i in range(len(p) - 1):
        print(f"{i:^7}|", end='')
    print('')
    print("p[i]|", end='')
    for i in range(len(p) - 1):
        print(f"{p[i]:>3}*{p[i + 1]:>3}|", end='')
    print('')

    diff = 0
    results, slices = matrix_chain_order(p)
    while diff < len(p) - 1:
        print(f"--- diff = {diff} ---")

        i, j = 0, diff
        while j < len(p) - 1:
            print(f"i = {i}, j = {j}, result = {results[i][j]}", end=' ')
            print_optimal_strategy(slices, i, j)
            print('')

            i += 1
            j += 1

        diff += 1
