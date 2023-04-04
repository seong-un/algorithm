import heapq

def dijkstra(s, e):
    least=[INF]*N
    least[s-1]=0
    heap=[]
    heapq.heappush(heap, [0, s-1])
    while heap:
        cost, a=heapq.heappop(heap)
        if a==e-1:
            return cost
        for i, c in hometown[a]:
            dist=c+cost
            if dist<least[i-1]:
                least[i-1]=dist
                heapq.heappush(heap, [dist, i-1])


T=int(input())
INF=int(1e9)
for test_case in range(1, T+1):
    N, M, X=map(int, input().split())
    hometown=[[] for i in range(N)]
    for i in range(M):
        a, b, cost=map(int, input().split())
        hometown[a-1].append((b, cost))
    party=0
    for i in range(N):
        party=max(party, dijkstra(i+1, X)+dijkstra(X, i+1))
    print(f'#{test_case} {party}')