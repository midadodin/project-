from collections import deque

n, m = list(map(int, input().split()))

events = []
for _ in range(m):
    start, end = list(map(int, input().split()))
    events.append([start, 1])
    events.append([end, -1])
events.sort()

queue = deque()
for event in events:
    queue.append(event)
print(queue)
start_queue = deque(events[i][0] for i in range(m) if events[i][1] == 1)
end_queue = deque(events[i][0] for i in range(m) if events[i][1] == -1)
current_position = 0
"""
while queue:
    next_event = queue.popleft()"""