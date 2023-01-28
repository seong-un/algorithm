import sys
input = sys.stdin.readline

ch=list(input().strip())
M=int(input())
sv=[]

for i in range(1, M+1):
  com=input().split()
  if com[0]=="L":
    if ch:sv.append(ch.pop())
  if com[0]=="D":
    if sv:ch.append(sv.pop())
  if com[0]=="B":
    if ch:ch.pop()
  if com[0]=="P":
    ch.append(com[1])
for i in range(1, len(sv)+1):
  ch.append(sv.pop())
print(''.join(ch))