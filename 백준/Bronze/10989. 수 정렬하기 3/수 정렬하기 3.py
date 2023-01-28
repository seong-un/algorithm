import sys
input=sys.stdin.readline

N=int(input())
sort_list=[0]*10001
for i in range(N):
  sort_list[int(input())]+=1
for i in range(10001):
  if sort_list[i]!=0:
    for j in range(sort_list[i]):
      print(i)