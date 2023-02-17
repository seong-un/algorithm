def involution(N, M):
  if M==1:
    return N
  return involution(N, M-1)*N

for _ in range(10):
  T=int(input())
  N, M=map(int, input().split())
  print(f'#{T} {involution(N, M)}')