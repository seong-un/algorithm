for _ in range(10):
    T, R=map(int, input().split())
    road=list(map(int, input().split()))
    route=[0]*(R)
    for i in range(R):
        route[i]=(road[2*i], road[2*i+1])
    rmap=[[] for i in range(100)]
    for i in route:
        rmap[i[0]].append(i[1])

    def DFS(graph, root):
        result=0
        visited=[]
        stack=[root]

        while stack:
            n=stack.pop()
            if n==99:
                result=1
            if n not in visited:
                visited.append(n)
                stack+=list(set(graph[n])-set(visited))
        return result

    print(f'#{T} {DFS(rmap, 0)}')