T=int(input())

for i in range(T):
  N=int(input())
  
  arr=[1,1,1,2,2]
  for i in range(5,N):
    arr.append(arr[i-5]+arr[i-1])
  
  print(arr[N-1])