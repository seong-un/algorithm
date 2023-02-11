N=int(input())
side=[0]*6
for i in range(6):
  side[i]=list(map(int, input().split()))
for i in range(6):
  if side[5-i][0]==side[3-i][0] and side[4-i][0]==side[2-i][0]:
    print((side[1-i][1]*side[-i][1]-side[3-i][1]*side[4-i][1])*N)