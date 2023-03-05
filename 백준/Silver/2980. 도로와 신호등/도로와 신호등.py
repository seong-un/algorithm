N, L=map(int, input().split())
light=[0]*N
for i in range(N):
  light[i]=list(map(int, input().split()))
light.insert(0, [0,0,0])
i=1
time=0
while i<=N:
  time+=light[i][0]-light[i-1][0]
  if time%(light[i][1]+light[i][2])<light[i][1]:
    time+=light[i][1]-time%(light[i][1]+light[i][2])
  i+=1
time+=L-light[i-1][0]
print(time)