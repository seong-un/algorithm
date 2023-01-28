K=int(input())

eco=[]
for i in range(1,K+1):
  eco.append(int(input()))
  if eco[-1]==0:
    eco.pop()
    eco.pop()
  else:pass
print(sum(eco))