from collections import deque

for test_case in range(1, 11):
    N, v=map(int, input().split())
    fromto=list(map(int, input().split()))
    contact=[[0]*100 for i in range(100)]
    for i in range(int(N/2)):
        contact[fromto[2*i]-1][fromto[2*i+1]-1]=1
    queue=deque([v-1])
    cnt=[0]*100
    cnt[v-1]=1
    while queue:
        a=queue.popleft()
        for idx, i in enumerate(contact[a]):
            if i==1 and not cnt[idx]:
                queue.append(idx)
                cnt[idx]=cnt[a]+1
    last=[]
    for idx, i in enumerate(cnt):
        if i==max(cnt):
            last.append(idx+1)
    print(f'#{test_case} {max(last)}')