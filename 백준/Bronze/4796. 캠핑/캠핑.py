L ,P, V,i=1,1,1,0
while not (L==0 and P==0 and V==0):
  L,P,V=map(int, input().split())
  if L==0 and P==0 and V==0:
    pass
  else:
    i+=1
    print("Case %d:"%i, (V//P)*L+min(L, V%P))