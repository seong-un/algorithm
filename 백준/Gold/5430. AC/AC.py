from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(T):
    p = input().strip()
    n = int(input().strip())
    str_x = input().strip()
    queue_x = deque(str_x.replace("[", "").replace("]", "").split(","))
    if queue_x[0] == '':
        queue_x = deque()

    R = False
    for i in p:
        if i == "R":
            R = not R
        else:
            try:
                if R:
                    queue_x.pop()
                else:
                    queue_x.popleft()
            except:
                queue_x = "error"
                break
                
    if queue_x != "error":
        if R:
            queue_x.reverse()
        print("[" + ','.join(queue_x) + "]")
    else:
        print(queue_x)