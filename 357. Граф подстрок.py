from collections import defaultdict

def create_graph(lines):
    graph = defaultdict(int)
    count = set()
    for line in lines:
        words = [line[i:i + 3] for i in range(len(line) - 2)]
        for i in range(len(words) - 1):
            graph[(words[i], words[i + 1])] += 1
            count.add(words[i])
        count.add(words[-1])
    return graph, len(count)

n = int(input())

lines = [input() for _ in range(n)]

graph, count = create_graph(lines)
print(count)
print(len(graph))
for key, value in graph.items():
    print(*key, value)