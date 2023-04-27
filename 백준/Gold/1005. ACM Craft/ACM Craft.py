import heapq
from collections import deque

def dijkstra(start):
    que = deque()
    que.append(start)
    d[start] = times[start]

    while que:
        now = que.popleft()
        
        if nodes_rev[now]:
            for node in nodes_rev[now]:
            
                if d[node] < d[now] + times[node]:
                    d[node] = d[now] + times[node]
                    que.append(node)


T = int(input())

for i in range(T):
    N, K = map(int,input().split())
    
    times = [0] + list(map(int,input().split()))
    d = [0 for _ in range(N+1)]

    nodes_rev = [[] for _ in range(N+1)]
    for _ in range(K):
        s, e = map(int,input().split())
        # nodes[s] += [[e,-1*times[s]]]
        nodes_rev[e].append(s)
        
    end = int(input())

    dijkstra(end)
    print(max(d))