from collections import deque

for _ in range(10):
    test_case=int(input())
    maze=[0]*16
    for i in range(16):
        maze[i]=list(map(int, input()))
        if 2 in maze[i]:
            a, b=i, maze[i].index(2)
    queue=deque()
    queue.append([int(a),int(b)])
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    result=0
    while queue:
        q=queue.popleft()
        maze[q[0]][q[1]]=2
        for i in range(4):
            nx=q[0]+dx[i]
            ny=q[1]+dy[i]
            if nx<0 or ny<0 or nx>15 or ny>15 or maze[nx][ny]==1 or maze[nx][ny]==2:
                continue
            elif maze[nx][ny]==0:
                queue.append([nx, ny])
            elif maze[nx][ny]==3:
                result=1
                break
        if result==1:
            break
    print(f'#{test_case} {result}')