N=int(input())
for _ in range(N):
  a, *adisk=map(int, input().split())
  b, *bdisk=map(int, input().split())
  disk=4
  while disk>0:
    if adisk.count(disk)>bdisk.count(disk):
      print('A')
      break
    elif adisk.count(disk)<bdisk.count(disk):
      print('B')
      break
    else:
      disk-=1
  if disk==0:
    print('D')