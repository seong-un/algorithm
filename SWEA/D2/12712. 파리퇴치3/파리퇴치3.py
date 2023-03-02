T=int(input())
for test_case in range(1, T+1):
    N, M=map(int, input().split())
    fly=[0]*N
    for i in range(N):
        fly[i]=list(map(int, input().split()))
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    dxx=[-1, -1, 1, 1]
    dyy=[-1, 1, -1, 1]
    Fkiller=[]
    for i in range(N):
        for j in range(N):
            sm=fly[i][j]
            for k in range(4):
                for m in range(1, M):
                    nx=i+dx[k]*m
                    ny=j+dy[k]*m
                    if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                        continue
                    sm+=fly[nx][ny]
            Fkiller.append(sm)
            sm=fly[i][j]
            for k in range(4):
                for m in range(1, M):
                    nx=i+dxx[k]*m
                    ny=j+dyy[k]*m
                    if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                        continue
                    sm+=fly[nx][ny]
            Fkiller.append(sm)
    print(f'#{test_case} {max(Fkiller)}')