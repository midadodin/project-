def main():
    m = int(input())
    n = int(input())

    if n < 2:
        print(n)
        return

    intervals = []

    for _ in range(n):
        intervals.append(list(map(int, input().split())))

    intervals.sort()
    stack = []

    for start, end in intervals:
        if not stack or stack[-1][1] < start:
            stack.append([start, end])
        else:
            stack[-1][1] = max(stack[-1][1], end)
    
    print(len(stack))

main()