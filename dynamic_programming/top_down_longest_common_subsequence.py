import sys


def lcs_length(x, y, idx_of_start, idx_of_end):
    results = [[-sys.maxsize for _ in range(max(len(x), len(y)))]
               for _ in range(max(len(x), len(y)))]

    return lcs_length_internal(x, y, idx_of_start, idx_of_end, results)


def lcs_length_internal(x, y, idx_of_start, idx_of_end, results):
    if results[idx_of_start][idx_of_end] > -sys.maxsize:
        return results[idx_of_start][idx_of_end]

    if idx_of_start == 0 and idx_of_end == 0:
        if x[0] == y[0]:
            result = 1
        else:
            result = 0
    elif idx_of_start == 0:
        result = 1 if x[0] == y[idx_of_end] else lcs_length_internal(
            x, y, idx_of_start, idx_of_end - 1, results)
    elif idx_of_end == 0:
        result = 1 if x[idx_of_start] == y[0] else lcs_length_internal(
            x, y, idx_of_start - 1, idx_of_end, results)
    else:
        if x[idx_of_start] == y[idx_of_end]:
            result = lcs_length_internal(
                x, y, idx_of_start - 1, idx_of_end - 1, results) + 1
        else:
            result = max(lcs_length_internal(x, y, idx_of_start - 1, idx_of_end, results),
                         lcs_length_internal(x, y, idx_of_start, idx_of_end - 1, results))

    results[idx_of_start][idx_of_end] = result

    return result


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i, _x in enumerate(x):
        print(f"--- i = {i} ---")
        for j, _y in enumerate(y):
            result = lcs_length(x, y, i, j)

            print(f"i = {i}, j = {j}, x = {x[:i + 1]}, "
                  f"y = {y[:j + 1]} / result = {result}")
