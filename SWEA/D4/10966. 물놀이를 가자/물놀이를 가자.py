from collections import deque

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    summer = [[-1] * M for i in range(N)]
    queue=deque()
    for i in range(N):
        a = list(input())
        for j in range(M):
            if a[j]=='W':
                summer[i][j]=0
                queue.append((i,j))
 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or summer[nx][ny]!=-1:
                continue
            queue.append((nx, ny))
            summer[nx][ny]=summer[a][b]+1
      
    result=0
    for i in summer:
        result+=sum(i)
    print(f'#{test_case} {result}')