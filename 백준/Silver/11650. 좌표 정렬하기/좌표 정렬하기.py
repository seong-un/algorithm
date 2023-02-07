N=int(input())
coordinate=[]
for _ in range(N):
    coordinate.append(list(map(int, input().split())))
coordinate=sorted(coordinate, key=lambda x:(x[0], x[1]))
for i in coordinate:
    print(*i)