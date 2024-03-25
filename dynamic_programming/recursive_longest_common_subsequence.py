if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i, _x in enumerate(x):
        print(f"--- i = {i} ---")
        for j, _y in enumerate(y):
            print(f"i = {i}, j = {j}, x = {x[:i + 1]}, y = {y[:j + 1]}")
