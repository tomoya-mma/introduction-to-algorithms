def search(key, data):
    idx_of_left = 0
    idx_of_right = len(data) - 1

    while idx_of_left <= idx_of_right:
        idx_of_middle = (idx_of_left + idx_of_right) // 2
        if data[idx_of_middle] == key:
            return idx_of_middle
        elif data[idx_of_middle] < key:
            idx_of_left = idx_of_middle + 1
        else:
            idx_of_right = idx_of_middle - 1

    return -1


if __name__ == '__main__':
    data = [2 ** i for i in range(20)]
    print(data)

    print("input key > ", end='')
    key = int(input())

    result = search(key, data)
    if result == -1:
        print(f"{key} is not found.")
    else:
        print(f"result = {result}")
