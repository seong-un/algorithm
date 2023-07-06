from collections import deque

n, w, L = map(int, input().split())
truck = deque(map(int, input().split()))

bridge = deque([0] * w)
count = 0
while truck:
    bridge.append(truck.popleft())
    bridge.popleft()
    if sum(bridge) > L:
        truck.appendleft(bridge.pop())
        bridge.append(0)
    count += 1
print(count + w)