from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

q = deque()
ans = []

for i in range(n):
    # Удаляем элементы из начала дека, которые больше текущего элемента
    while q and a[q[-1]] >= a[i]:
        q.pop()
    
    # Добавляем текущий элемент в конец дека
    q.append(i)
    
    # Если окно достигло размера k, добавляем минимум в ответ
    if i >= k - 1:
        ans.append(a[q[0]])
        
        # Удаляем элементы из начала дека, которые выходят за пределы окна
        if q[0] <= i - k + 1:
            q.popleft()

for a in ans:
    print(a)