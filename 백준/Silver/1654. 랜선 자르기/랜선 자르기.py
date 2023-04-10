K, N= map(int, input().split())
lan=[0]*K
for i in range(K):
    lan[i]=int(input())
start = 1
end = max(lan)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt > N:
        start = mid + 1
    elif cnt < N:
        end = mid - 1
    else:
        mid += 1
        for i in lan:
            cnt -= i // mid
        if cnt == 0:
            start = mid
        else:
            break
cnt=0
for i in lan:
    cnt+=i//mid
if cnt>=N:
    print(mid)
else:
    print(mid-1)