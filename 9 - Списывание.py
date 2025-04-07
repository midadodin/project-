def main():
    line = list(map(int, input().split()))
    n, m = line[0], line[1]
    pairs = []
    colors = {}

    for i in range(m):
        pairs.append(list(map(int, input().split())))
    for k in range(n):
        for i in range(m):
            if colors.get(pairs[i][0]) is None and colors.get(pairs[i][1]) is None:
                colors[pairs[i][0]] = 1
                colors[pairs[i][1]] = -1
            elif colors.get(pairs[i][0]) is not None and colors.get(pairs[i][1]) is not None:
                if colors[pairs[i][0]] * colors[pairs[i][1]] > 0:
                    print('NO')
                    return
                else:
                    continue
            elif colors.get(pairs[i][0]) is not None:
                if colors[pairs[i][0]] == 1:
                    colors[pairs[i][1]] = -1
                elif colors[pairs[i][0]] == -1:
                    colors[pairs[i][1]] = 1
            elif colors.get(pairs[i][1]) is not None:
                if colors[pairs[i][1]] == 1:
                    colors[pairs[i][0]] = -1
                elif colors[pairs[i][1]] == -1:
                    colors[pairs[i][0]] = 1

    for i in range(m):
        if colors[pairs[i][0]] * colors[pairs[i][1]] > 0:
            print('NO')
            return
        else:
            continue
    print('YES')

if __name__ == "__main__":
    main()