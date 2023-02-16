T=int(input())
for test_case in range(1, T+1):
    N, M=map(int, input().split())
    pan=[[0]*N for i in range(N)]
    pan[N//2-1][N//2-1]=pan[N//2][N//2]=2
    pan[N//2][N//2-1]=pan[N//2-1][N//2]=1
    dx=[-1, 1, 0, 0, -1, 1, -1, 1]
    dy=[0, 0, -1, 1, -1, 1, 1, -1]
    for i in range(M):
        a,b,color=map(int, input().split())
        a, b=b-1, a-1
        pan[a][b]=color
        for j in range(8):
            nx=a+dx[j]
            ny=b+dy[j]
            if nx<0 or ny<0 or nx>N-1 or ny>N-1 or pan[nx][ny] in [0, color]:
                continue
            for k in range(2, N):
                if a+dx[j]*k<0 or b+dy[j]*k<0 or a+dx[j]*k>N-1 or b+dy[j]*k>N-1:
                    continue
                if pan[a+dx[j]*k][b+dy[j]*k]==0:
                    break
                if pan[a+dx[j]*k][b+dy[j]*k]==color:
                    for pn in range(1, k):
                        pan[a+dx[j]*pn][b+dy[j]*pn]=color
                    break
    cnt=[0]*2
    for i in pan:
        cnt[0]+=i.count(1)
        cnt[1]+=i.count(2)
    print(f'#{test_case}', *cnt)