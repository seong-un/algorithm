T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    A=[list(map(int, input().split())) for i in range(N)]
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    visited=set() # 방문했던 방
    room=[] # 어떤 방에서 얼만큼의 방을 이동했는지
    for i in range(N):
        for j in range(N):
            if (i, j) in visited:
                continue
            a, b=i, j
            visited.add((a,b))
            cnt=1
            track=True
            while track:
                for k in range(4):
                    nx=a+dx[k]
                    ny=b+dy[k]
                    if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                        if k == 3:
                            track = False
                        continue
                    if A[a][b]==A[nx][ny]-1:
                        a, b=nx, ny
                        visited.add((a,b))
                        cnt+=1
                        break
                    if k==3:
                        track=False
            room.append((A[i][j], cnt))
    m=max(room, key=lambda x:x[1])[1]
    room_number=N**2
    for i in room:
        if i[1]==m:
            room_number=min(room_number, i[0])
    print(f'#{test_case} {room_number} {m}')