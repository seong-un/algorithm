from collections import deque

T=int(input())
for test_case in range(1, T+1):
    N, M, R, C, L=map(int, input().split())
    ternel=[0]*N
    for i in range(N):
        ternel[i]=list(map(int, input().split()))
    queue=deque()
    queue.append([R, C])
    visited=[[False]*M for i in range(N)]
    visited[R][C]=1
    for_break=0
    while not for_break and queue:
        a=queue.popleft()
        if ternel[a[0]][a[1]]==1:
            dx=[-1, 1, 0, 0]
            dy=[0, 0, -1, 1]
        elif ternel[a[0]][a[1]]==2:
            dx=[-1, 1]
            dy=[0, 0]
        elif ternel[a[0]][a[1]]==3:
            dx=[0, 0]
            dy=[-1, 1]
        elif ternel[a[0]][a[1]]==4:
            dx=[-1, 0]
            dy=[0, 1]
        elif ternel[a[0]][a[1]]==5:
            dx=[1, 0]
            dy=[0, 1]
        elif ternel[a[0]][a[1]]==6:
            dx=[1, 0]
            dy=[0, -1]
        else:
            dx=[-1, 0]
            dy=[0, -1]
        if ternel[a[0]][a[1]]==1:
            coin=4
        else:
            coin=2
        for i in range(coin):
            nx=a[0]+dx[i]
            ny=a[1]+dy[i]
            if nx<0 or ny<0 or nx>N-1 or ny>M-1 or not ternel[nx][ny] or visited[nx][ny]:
                continue
            if (dx[i]==-1 and ternel[nx][ny] in [1,2,5,6]) or (dx[i]==1 and ternel[nx][ny] in [1,2,4,7]) or (dy[i]==-1 and ternel[nx][ny] in [1,3,4,5]) or (dy[i]==1 and ternel[nx][ny] in [1,3,6,7]):
                queue.append([nx, ny])
                if visited[a[0]][a[1]]==L:
                    for_break=1
                    break
                visited[nx][ny]=visited[a[0]][a[1]]+1
    prisoner=0
    for i in visited:
        for j in i:
            if j:
                prisoner+=1
    print(f'#{test_case} {prisoner}')