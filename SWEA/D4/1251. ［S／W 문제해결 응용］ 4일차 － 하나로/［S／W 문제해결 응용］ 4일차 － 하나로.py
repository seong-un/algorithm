import heapq

T = int(input())
INF = int(1e9)
for test_case in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    heap=[]
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            heapq.heappush(heap, [(X[i]-X[j])**2+(Y[i]-Y[j])**2, i, j])
    cost=0
    cnt=0
    union=[[i] for i in range(N)]
    while cnt<N-1:
        least, a, b=heapq.heappop(heap)
        con=False
        for i in union:
            if a in i:
                if b in i:
                    con=True
                    break
                break
        if con:
            continue
        cost+=least
        cnt+=1
        for idx, i in enumerate(union):
            if a in i:
                ai=idx
            if b in i:
                bi=idx
        union[ai]+=union[bi]
        del union[bi]
    print(f'#{test_case} {round(E*cost)}')