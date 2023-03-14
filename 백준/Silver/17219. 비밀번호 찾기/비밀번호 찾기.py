import sys
input=sys.stdin.readline

N, M= map(int, input().split())
links=dict()
for i in range(N):
  link, name=list(input().rstrip().split())
  links[link]=name
for i in range(M):
  password=input().rstrip()
  print(links[password])