X=input()

t=0
while len(str(X))!=1:
  X=sum(map(int, str(X)))
  t+=1

print(t)
if int(X)%3==0:
  print("YES")
else:
  print("NO")