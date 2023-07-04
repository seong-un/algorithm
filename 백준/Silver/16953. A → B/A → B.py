from collections import deque

A, B = map(int, input().split())

queue=deque([(A, 1)])
for_break = False
while queue:
    a, count = queue.popleft()
    if a == B:
        print(count)
        for_break = True
        break
    if 2 * a <= B:
        queue.append((a * 2, count + 1))
    if 10 * a + 1 <= B:
        queue.append((10 * a + 1, count + 1))

if not for_break:
    print(-1)