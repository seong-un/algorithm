from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
stack=deque()
for _ in range(N):
    command=list(input().split())
    if command[0]=='push':
        stack.append(int(command[1]))
    if command[0]=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if command[0]=='size':
        print(len(stack))
    if command[0]=='empty':
        if stack:
            print(0)
        else:
            print(1)
    if command[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)