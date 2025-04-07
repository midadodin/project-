def main():
    n = int(input())
    m = int(input())
    lines = []
    visited = []
    stations = {}
    all_stations = [i for i in range(1, n + 1)]

    for i in range(m):
        lines.append(list(map(int, input().split()[1:])))

    numbers = list(map(int, input().split()))
    start, stop = numbers[0], numbers[1]

    for i in range(m):
        for j in range(len(lines[i])):
            if start in lines[i]:
                stations[lines[i][j]] = 0
            elif stations.get(lines[i][j]) is None:
                stations[lines[i][j]] = n * m
                
    for k in range(n):
        for i in range(m):
            for station in stations:
                if station in lines[i]:
                    for j in range(len(lines[i])):
                        if stations[lines[i][j]] > stations[station] + 1:
                            stations[lines[i][j]] = stations[station] + 1

    if stations[stop] == n * m:
        print(-1)
    else:
        print(stations[stop])
    
        
if __name__ == '__main__':
    main()