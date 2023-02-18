N, r, c=map(int, input().split())
start=0
end=2**(2*N)-1
while start!=end:
  if r//(2**(N-1))%2==0:
    end=(start+end)//2
  else:
    start=(start+end)//2+1
    r=r-r//(2**(N-1))*(2**(N-1))
  if c//(2**(N-1))%2==0:
    end=(start+end)//2
  else:
    start=(start+end)//2+1
    c=c-c//(2**(N-1))*(2**(N-1))
  N-=1
print(start)