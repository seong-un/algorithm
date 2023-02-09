horizon, vertex=map(int, input().split())
number=int(input())
lines=[0]*number
for i in range(number):
    lines[i]=list(map(int, input().split()))
lines=sorted(lines, key=lambda x:x[1])

hor, ver=[0],[0]
for j in range(len(lines)):
        if lines[j][0]==0:
            ver.append(lines[j][1]-sum(ver))
        else:
            hor.append(lines[j][1]-sum(hor))
hor.append(horizon-sum(hor))
ver.append(vertex-sum(ver))
hor=hor[1:]
ver=ver[1:]
area=[]
for i in hor:
    for j in ver:
        area.append(i*j)
print(max(area))