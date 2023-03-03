N, E=map(int, input().split())
graph=[[999999999]*N for i in range(N)]
for i in range(E):
    start, end, cost=map(int, input().split())
    graph[start-1][end-1]=cost
    graph[end-1][start-1]=cost
v1, v2=map(int, input().split())
result1=0
a=0
if v1!=1:
    visited=[]
    least=[999999999]*N
    least[a]=0
    while True:
        visited.append(a)
        for idx, i in enumerate(graph[a]):
            least[idx]=min(least[idx], least[a]+i)
        mn=[]
        for idx, i in enumerate(least):
            if idx not in visited:
                mn.append([i, idx])
        a=min(mn, key=lambda x:x[0])[1]
        if a==v1-1:
            result1+=least[a]
            break

if v2!=N:
    visited=[]
    least=[999999999]*N
    least[a]=0
    while True:
        visited.append(a)
        for idx, i in enumerate(graph[a]):
            least[idx]=min(least[idx], least[a]+i)
        mn=[]
        for idx, i in enumerate(least):
            if idx not in visited:
                mn.append([i, idx])
        a=min(mn, key=lambda x:x[0])[1]
        if a==v2-1:
            result1+=least[a]
            break

visited=[]
least=[999999999]*N
least[a]=0
while True:
    visited.append(a)
    for idx, i in enumerate(graph[a]):
        least[idx]=min(least[idx], least[a]+i)
    mn=[]
    for idx, i in enumerate(least):
        if idx not in visited:
            mn.append([i, idx])
    a=min(mn, key=lambda x:x[0])[1]
    if a==N-1:
        result1+=least[a]
        break

result2=0
a=0
if v1!=1:
    visited=[]
    least=[999999999]*N
    least[a]=0
    while True:
        visited.append(a)
        for idx, i in enumerate(graph[a]):
            least[idx]=min(least[idx], least[a]+i)
        mn=[]
        for idx, i in enumerate(least):
            if idx not in visited:
                mn.append([i, idx])
        a=min(mn, key=lambda x:x[0])[1]
        if a==v2-1:
            result2+=least[a]
            break

if v2!=N:
    visited=[]
    least=[999999999]*N
    least[a]=0
    while True:
        visited.append(a)
        for idx, i in enumerate(graph[a]):
            least[idx]=min(least[idx], least[a]+i)
        mn=[]
        for idx, i in enumerate(least):
            if idx not in visited:
                mn.append([i, idx])
        a=min(mn, key=lambda x:x[0])[1]
        if a==v1-1:
            result2+=least[a]
            break

visited=[]
least=[999999999]*N
least[a]=0
while True:
    visited.append(a)
    for idx, i in enumerate(graph[a]):
        least[idx]=min(least[idx], least[a]+i)
    mn=[]
    for idx, i in enumerate(least):
        if idx not in visited:
            mn.append([i, idx])
    a=min(mn, key=lambda x:x[0])[1]
    if a==N-1:
        result2+=least[a]
        break

if min([result1, result2])>=999999999:
    print(-1)
else:
    print(min([result1, result2]))