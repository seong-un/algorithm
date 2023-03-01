import sys
input=sys.stdin.readline

N, M=map(int, input().split())
nosound=set()
for i in range(N):
    nosound.add(input().rstrip())
invisible=set()
for i in range(M):
    invisible.add(input().rstrip())
jap=nosound&invisible
print(len(jap))
for i in sorted(jap):
    print(i)