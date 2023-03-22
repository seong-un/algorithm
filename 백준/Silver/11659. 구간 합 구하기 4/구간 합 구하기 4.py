import sys
input=sys.stdin.readline

N, M= map(int, input().split())
nature=[0]+list(map(int, input().split()))
for i in range(1, N+1):
    nature[i]+=nature[i-1]
for i in range(M):
    start, end=map(int, input().split())
    print(nature[end]-nature[start-1])