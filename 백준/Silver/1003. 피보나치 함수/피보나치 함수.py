T=int(input())
for _ in range(T):
  N=int(input())
  if N==0:
    print(1, 0)
  elif N==1:
    print(0, 1)
  else:
    lst=[1, 1]
    for i in range(N-2):
      lst.append(lst[i]+lst[i+1])
    print(lst[-2], lst[-1])