T=int(input())

for i in range(T):
  n=int(input())
  
  arr=[1, 2, 4]
  for i in range(3, n):
    arr.append(arr[i-3]+arr[i-2]+arr[i-1])
  
  print(arr[n-1])