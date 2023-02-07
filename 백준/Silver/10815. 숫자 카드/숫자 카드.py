import sys
input=sys.stdin.readline

N=int(input())
sangkeun=set(map(int, input().split()))
M=int(input())
check=list(map(int, input().split()))
result=[]
for i in check:
    if i in sangkeun:
        result.append(1)
    else:
        result.append(0)
print(*result)