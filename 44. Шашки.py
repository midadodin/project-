def main():
    n, m = list(map(int, input().split()))

    w = int(input())
    whites = []
    for _ in range(w):
        whites.append(list(map(int, input().split())))

    b = int(input())
    blackes = []
    for _ in range(w):
        blackes.append(list(map(int, input().split())))

    if input() == 'white':
        turn = whites
        opposite = blackes
    else:
        turn = blackes
        opposite = whites

    for x, y in turn:
        cells_to_check = [(x + 1, y + 1),
                        (x - 1, y + 1),
                        (x + 1, y - 1),
                        (x - 1, y - 1)]
        block_cells = [(x + 2, y + 2),
                    (x - 2, y + 2),
                    (x + 2, y - 2),
                    (x - 2, y - 2)]
        for i in range(4):
            new_x, new_y = cells_to_check[i]
            block_x, block_y = block_cells[i]

            if [new_x, new_y] in opposite and [block_x, block_y] not in opposite and [block_x, block_y] not in turn:
                return 'yes'
    return 'no'

print(main())