import sys
from collections import deque
input=sys.stdin.readline

def check(i, j):
    for k in queen:
        if k[1]==j:
            return False
        if k[0]-k[1]==i-j:
            return False
        if k[0]+k[1]==i+j:
            return False
    return True


def Queen(i, N):
    global cnt
    if i==N:
        cnt+=1
        return
    for j in range(N):
        if check(i, j):
            queen.append((i,j))
            Queen(i+1,N)
            queen.pop()

N=int(input())
cnt=0
queen=deque()
dx=[-1, 1]
dy=[1, -1]
Queen(0, N)
print(cnt)