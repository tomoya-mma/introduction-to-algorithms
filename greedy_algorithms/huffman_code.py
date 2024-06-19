import heapq


class Node:

    __slots__ = ['ch', 'frequency', 'left', 'right']

    def __init__(self):
        self.ch = None
        self.frequency = 0
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.ch if self.ch else ''} ({self.frequency})"

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman(characters, frequencies):
    nodes = [Node() for _ in range(len(characters))]

    for i, (ch, freq) in enumerate(zip(characters, frequencies)):
        nodes[i].ch = ch
        nodes[i].frequency = freq

    heapq.heapify(nodes)

    n = len(nodes)
    for i in range(n - 1):
        x = heapq.heappop(nodes)
        y = heapq.heappop(nodes)
        z = Node()
        z.frequency = x.frequency + y.frequency
        z.left = x
        z.right = y

        heapq.heappush(nodes, z)

    return heapq.heappop(nodes)


def print_tree(root):

    def print_tree_internal(r, space_size=0):
        if r.left:
            print_tree_internal(r.left, space_size=space_size+1)

        print('  ' * space_size, r)

        if r.right:
            print_tree_internal(r.right, space_size=space_size+1)

    print_tree_internal(root)


if __name__ == '__main__':
    characters = ['a', 'b', 'c', 'd', 'e', 'f']
    frequencies = [45, 13, 12, 16, 9, 5]

    print('  i |', end='')
    for i in range(len(characters)):
        print(f"{i:^3}|", end='')
    print('')
    print('c[i]|', end='')
    for ch in characters:
        print(f"{ch:^3}|", end='')
    print('')
    print('f[i]|', end='')
    for f in frequencies:
        print(f"{f:^3}|", end='')
    print('')

    root = huffman(characters, frequencies)

    print_tree(root)
