import sys


def optimal_bst(p, q):
    results = [[-sys.maxsize for _ in range(len(p) + 1)]
               for _ in range(len(p) + 1)]
    roots = [[-1 for _ in range(len(p) + 1)] for _ in range(len(p) + 1)]
    w = [[-1 for _ in range(len(p) + 1)] for _ in range(len(p) + 1)]

    for l in range(1, len(p) + 1):
        results[l][l - 1] = q[l - 1]
        w[l][l - 1] = q[l - 1]

    diff = 0
    while diff < len(p) - 1:
        i = 1
        j = i + diff

        while j < len(p):
            w[i][j] = round(w[i][j - 1] + p[j] + q[j], 2)

            result = sys.maxsize
            for r in range(i, j + 1):
                if result > results[i][r - 1] + results[r + 1][j] + w[i][j]:
                    result = results[i][r - 1] + results[r + 1][j] + w[i][j]
                    roots[i][j] = r

            results[i][j] = result

            i += 1
            j += 1

        diff += 1

    return results, roots, w


if __name__ == '__main__':
    p = [0.0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

    print("  i |", end='')
    for i in range(len(p)):
        print(f"{i:>4}|", end='')
    print('')
    print("p[i]|", end='')
    for _p in p:
        print(f"{_p:>4}|", end='')
    print('')
    print("q[i]|", end='')
    for _q in q:
        print(f"{_q:>4}|", end='')
    print('')

    results, roots, w = optimal_bst(p, q)

    diff = -1
    while diff < len(p) - 1:
        print(f"--- diff = {diff} ---")

        i = 1
        j = i + diff
        while j < len(p):
            print(f"i = {i}, j = {j} "
                  f"/ result = {results[i][j]:.2f}, "
                  f"root = {roots[i][j] if roots[i][j] != -1 else '-'}, "
                  f"w = {w[i][j]:.2f}")

            i += 1
            j += 1

        diff += 1
