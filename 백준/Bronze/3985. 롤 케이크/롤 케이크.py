L=int(input())
N=int(input())
roll=[0]*(L+1)
audience=[0]*N
for i in range(N):
  audience[i]=list(map(int, input().split()))
expect=[0]*N
for idx, i in enumerate(reversed(audience)):
  expect[idx]=audience[idx][1]-audience[idx][0]
  roll[i[0]:i[1]+1]=[N-idx]*(i[1]-i[0]+1)
print(expect.index(max(expect))+1)
mx=-1
for i in range(N):
  if roll.count(mx)<roll.count(i+1):
    mx=i+1
print(mx)