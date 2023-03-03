T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    concave=[0]*N
    for i in range(N):
        concave[i]=input()
    dx=[1, 0, -1, 1, 1]
    dy=[0, 1, 1, -1, 1]
    omok=False
    for i in range(N):
        for j in range(N):
            if concave[i][j]=='o':
                for k in range(5):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if nx<0 or ny<0 or nx>N-1 or ny>N-1 or concave[nx][ny]=='.':
                        continue
                    for c in range(2, 5):
                        if 0<=i+dx[k]*c<N and 0<=j+dy[k]*c<N:
                            if concave[i+dx[k]*c][j+dy[k]*c]=='o':
                                if c==4:
                                    omok=True
                                else:
                                    continue
                            else:
                                break
                    if omok:
                        break
            if omok:
                break
        if omok:
            break
    if omok:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')