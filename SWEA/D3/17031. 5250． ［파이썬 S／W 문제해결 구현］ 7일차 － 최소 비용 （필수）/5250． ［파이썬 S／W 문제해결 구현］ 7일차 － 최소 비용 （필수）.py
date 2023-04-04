import heapq

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    H=[list(map(int, input().split())) for i in range(N)]
    a,b=0,0
    least=[[999999999]*N for i in range(N)]
    least[a][b]=0
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    heap=[]
    heapq.heappush(heap, [least[a][b], a, b])
    while heap:
        for k in range(4):
            nx=a+dx[k]
            ny=b+dy[k]
            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                continue
            cost=least[a][b]+1
            if H[nx][ny]>H[a][b]:
                cost+=H[nx][ny]-H[a][b]
            if cost<least[nx][ny]:
                least[nx][ny]=cost
                heapq.heappush(heap, [cost, nx, ny])
        _, a, b=heapq.heappop(heap)
        if a==N-1 and b==N-1:
            print(f'#{test_case} {least[a][b]}')
            break