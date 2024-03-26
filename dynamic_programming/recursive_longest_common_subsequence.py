def lcs_length(x, y, idx_of_start, idx_of_end):
    if idx_of_start == 0 and idx_of_end == 0:
        return 1 if x[0] == y[0] else 0
    elif idx_of_start == 0:
        return 1 if x[0] == y[idx_of_end] else lcs_length(x, y, idx_of_start, idx_of_end - 1)
    elif idx_of_end == 0:
        return 1 if x[idx_of_start] == y[0] else lcs_length(x, y, idx_of_start - 1, idx_of_end)
    else:
        if x[idx_of_start] == y[idx_of_end]:
            return lcs_length(x, y, idx_of_start - 1, idx_of_end - 1) + 1
        else:
            return max(lcs_length(x, y, idx_of_start - 1, idx_of_end),
                       lcs_length(x, y, idx_of_start, idx_of_end - 1))


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i, _x in enumerate(x):
        print(f"--- i = {i} ---")
        for j, _y in enumerate(y):
            result = lcs_length(x, y, i, j)

            print(f"i = {i}, j = {j}, x = {x[:i + 1]}, "
                  f"y = {y[:j + 1]} / result = {result}")
