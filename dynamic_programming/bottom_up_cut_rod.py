import sys


def cut_rod(prices, n):
    results = [-sys.maxsize for _ in range(n + 1)]
    divisions = [-1 for _ in range(n + 1)]

    results[0] = 0

    for j in range(1, n):
        result = -sys.maxsize
        for i in range(j + 1):
            if result < prices[i] + results[j - i]:
                result = prices[i] + results[j - i]
                divisions[j] = i

        results[j] = result

    return results, divisions


def print_optimal_strategy(divisions, n):
    print('(', end='')

    rest = n
    while rest > 0:
        print(divisions[rest], end='')

        if rest - divisions[rest] > 0:
            print(' + ', end='')

        rest -= divisions[rest]

    print(')', end='')


if __name__ == '__main__':
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    print("  i |", end='')
    for i in range(len(prices)):
        print(f"{i:>3}|", end='')
    print('')
    print("p[i]|", end='')
    for p in prices:
        print(f"{p:>3}|", end='')
    print('')

    results, divisions = cut_rod(prices, len(prices))
    for i in range(len(prices)):
        print(f"length = {i} / result = {results[i]}", end=' ')

        if i != 0:
            print_optimal_strategy(divisions, i)

        print('')
