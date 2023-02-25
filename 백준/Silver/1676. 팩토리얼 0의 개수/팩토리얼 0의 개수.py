N=int(input())
cnt2=cnt5=0
for i in range(1, N+1):
  a=i
  while True:
    if a%2==0:
      a/=2
      cnt2+=1
    if a%5==0:
      a/=5
      cnt5+=1
    if a%2!=0 and a%5!=0:
      break
print(min(cnt2, cnt5))