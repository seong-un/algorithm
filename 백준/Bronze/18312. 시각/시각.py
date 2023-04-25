N, K=map(int, input().split())
hours=[str(i) for i in range(N+1)]
for idx, i in enumerate(hours):
    if len(i)==1:
        hours[idx]='0'+i
minutes=[str(i) for i in range(60)]
for idx, i in enumerate(minutes):
    if len(i)==1:
        minutes[idx]='0'+i
seconds=minutes[:]
times=[]
for h in hours:
    for m in minutes:
        for s in seconds:
            times.append(h+m+s)
total=0
for i in times:
    if str(K) in i:
        total+=1
print(total)