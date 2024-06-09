import sys


def cut_rod(prices):
    results = [-sys.maxsize for _ in range(len(prices) + 1)]
    slices = [-1 for _ in range(len(prices) + 1)]

    results[0] = 0
    for j in range(1, len(prices)):
        result = -sys.maxsize
        for i in range(j + 1):
            if result < prices[i] + results[j - i]:
                result = prices[i] + results[j - i]
                slices[j] = i

        results[j] = result

    return results, slices


def print_optimal_strategy(slices, n):
    rest = n

    while rest > 0:
        print(slices[rest], end='')
        if rest - slices[rest] > 0:
            print(' + ', end='')

        rest -= slices[rest]


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

    results, slices = cut_rod(prices)
    for i in range(len(prices)):
        print(f"length = {i} / result = {results[i]} ", end='')

        if i != 0:
            print('(', end='')
            print_optimal_strategy(slices, i)
            print(')', end='')

        print('')
