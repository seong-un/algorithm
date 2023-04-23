N=int(input())
build = [list(map(int, list(input().split()))) for i in range(N)]
rank = [1]*N
for idx, i in enumerate(build):
    for j in build:
        if i[0]<j[0] and i[1]<j[1]:
            rank[idx]+=1
print(*rank)