import sys
input=sys.stdin.readline

N, M=map(int, input().split())
numbers=[[] for i in range(N)]
for i in range(N):
    numbers[i]=[0]+list(map(int, input().split()))
    for j in range(1, N+1):
        numbers[i][j]=numbers[i][j-1]+numbers[i][j]

for _ in range(M):
    x1, y1, x2, y2=map(int, input().split())
    sm=0
    for i in range(x1-1, x2):
        sm+=numbers[i][y2]-numbers[i][y1-1]
    print(sm)