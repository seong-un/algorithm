import heapq

T=int(input())
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
INF=int(1e9)
for test_case in range(1, T+1):
    N=int(input())
    Map=[list(map(int, list(input()))) for i in range(N)]
    least=[[INF]*N for i in range(N)]
    a,b=0,0
    least[a][b]=0
    heap=[]
    heapq.heappush(heap, [0, a, b])
    while heap:
        cost, a, b=heapq.heappop(heap)
        if a==N-1 and b==N-1:
            print(f'#{test_case} {cost}')
            break
        for k in range(4):
            nx=a+dx[k]
            ny=b+dy[k]
            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                continue
            dist=least[a][b]+Map[nx][ny]
            if dist<least[nx][ny]:
                least[nx][ny]=dist
                heapq.heappush(heap, [dist, nx, ny])