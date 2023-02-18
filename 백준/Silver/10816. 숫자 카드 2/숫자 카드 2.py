import sys
input=sys.stdin.readline

N=int(input())
card=list(map(int, input().split()))
M=int(input())
sangeun=list(map(int, input().split()))
card.sort()
lst=[0]*M
for idx, s in enumerate(sangeun):
  a=0
  b=-1
  start=0
  end=N-1
  while start<=end:
    mid=(start+end)//2
    if card[mid]<s:
      start=mid+1
    elif card[mid]>s:
      end=mid-1
    else:
      if mid-1>=0:
        if card[mid-1]!=s:
          a=mid
          break
        else:
          end=mid-1
      else:
        a=mid
        break
  start=0
  end=N-1
  while start<=end:
    mid=(start+end)//2
    if card[mid]<s:
      start=mid+1
    elif card[mid]>s:
      end=mid-1
    else:
      if mid+1<=N-1:
        if card[mid+1]!=s:
          b=mid
          break
        else:
          start=mid+1
      else:
        b=mid
        break
  lst[idx]=b-a+1
print(*lst)