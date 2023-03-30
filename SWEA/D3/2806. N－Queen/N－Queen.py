def check(i, j):
    checkit=True
    for k in range(8):
        q=1
        while True:
            nx=i+dx[k]*q
            ny=j+dy[k]*q
            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                break
            if (nx, ny) in queen:
                checkit=False
            q+=1
    return checkit


def Queen(i, N):
    global cnt
    if i==N:
        cnt+=1
        return
    for j in range(N):
        if check(i, j):
            queen.append((i,j))
            Queen(i+1,N)
            del queen[queen.index((i,j))]

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    cnt=0
    queen=[]
    dx=[-1, 1, 0, 0, -1, -1, 1, 1]
    dy=[0, 0, -1, 1, -1, 1, -1, 1]
    Queen(0, N)
    print(f'#{test_case} {cnt}')