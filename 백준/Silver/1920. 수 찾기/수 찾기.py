N=int(input())
NA=list(map(int,input().split()))
M=int(input())
MA=list(map(int, input().split()))

NA=sorted(NA)
def binary(start, end, target):
  mid=(end-start)//2+start
  if start>end:
    return 0
  if target>NA[mid]:
    return binary(mid+1, end, target)
  if target<NA[mid]:
    return binary(start, mid-1, target)
  if target==NA[mid]:
    return 1

for i in range(M):
  print(binary(0, N-1, MA[i]))