N=input()
L=list(N)
S1=0
for i in range(int(len(N)/2)):
  S1+=int(L[i])
S2=0
for i in range(int(len(N)/2)):
  S2+=int(L[int(len(N)/2+i)])

if S1==S2:
  print("LUCKY")
else:
  print("READY")