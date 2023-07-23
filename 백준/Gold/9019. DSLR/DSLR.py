from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    queue = deque()
    queue.append([0, A])
    visited = [False] * 10000
    while queue:
        command, a = queue.popleft()

        if a == B:
            for i in str(command):
                if i == '1':
                    print('D', end='')
                elif i == '2':
                    print('S', end='')
                elif i == '3':
                    print('L', end='')
                else:
                    print('R', end='')
            print()
            break

        if 2*a >= 10000:
            if not visited[2*a % 10000]:
                queue.append([command*10 + 1, 2*a % 10000])
                visited[2*a % 10000] = True
        else:
            if not visited[2*a]:
                queue.append([command*10 + 1, 2*a])
                visited[2*a] = True

        if a == 0:
            if not visited[9999]:
                queue.append([command*10 + 2, 9999])
                visited[9999] = True
        else:
            if not visited[a-1]:
                queue.append([command*10 + 2, a-1])
                visited[a-1] = True

        r = (a % 1000) * 10 + (a // 1000)
        if command == 0 or command % 10 != 4:
            if not visited[r]:
                queue.append([command*10 + 3, r])
                visited[r] = True

        r = a // 10 + (a % 10) * 1000
        if command == 0 or command % 10 != 3:
            if not visited[r]:
                queue.append([command*10 + 4, r])
                visited[r] = True