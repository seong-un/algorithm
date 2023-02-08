N=int(input())
colored_paper=[0]*N
for i in range(N):
    colored_paper[i]=list(map(int, input().split()))
A=[set() for i in range(N)]
for idx, i in enumerate(colored_paper):
    for j in range(i[0], i[0]+i[2]):
        for k in range(i[1], i[1]+i[3]):
            A[idx].add((j,k))
area=[0]*N

for idx, i in enumerate(A):
    sum_area=set()
    for j in A[idx+1:]:
        sum_area=sum_area|j
    area[idx]=len(i)-len(i&sum_area)

for i in area:
    print(i)