N=int(input())

RGB1=list(map(int, input().split()))
for i in range(N-1):
  RGB2=list(map(int, input().split()))
  RGB1=[min(RGB1[1]+RGB2[0], RGB1[2]+RGB2[0]), min(RGB1[0]+RGB2[1], RGB1[2]+RGB2[1]), min(RGB1[0]+RGB2[2], RGB1[1]+RGB2[2])]
  
print(min(RGB1))