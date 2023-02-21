from itertools import product

N=int(input())
M=int(input())
if M>0:
  button={str(i) for i in range(10)}-set(input().split())
  nPr=set()
  for i in range(1, len(str(N))+2):
    permutation=product(button, repeat=i)
    nPr=nPr|set(permutation)
  click=abs(100-N)
  for p in list(nPr):
    click=min(abs(N-int(''.join(p)))+len(''.join(p)), click)
  print(click)
else:
  print(min(len(str(N)), abs(100-N)))