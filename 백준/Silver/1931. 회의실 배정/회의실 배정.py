N=int(input())
meetings=[[] for i in range(N)]
for i in range(N):
  meetings[i]=list(map(int, input().split()))
meetings=sorted(meetings, key=lambda x:(x[1], x[0]))
meeting=meetings[0]
cnt=1
for i in meetings[1:]:
  if i[0] in range(meeting[1]):
    continue
  meeting=i
  cnt+=1
print(cnt)