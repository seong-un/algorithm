import sys
input=sys.stdin.readline

N, M=map(int, input().split())
pocketmon=['']*N
for i in range(N):
    pocketmon[i]=input()
for i in range(M):
    problem=input()
    if problem[:-1].isdigit():
        print(pocketmon[int(problem)-1][:-1])
    else:
        print(pocketmon.index(problem)+1)