import sys
input=sys.stdin.readline

N=int(input())
integer=[0]*N
for i in range(N):
    integer[i]=int(input())
avg=sum(integer)/N
if avg>=0:
    if avg-int(avg)<0.5:
        print(int(avg))
    else:
        print(int(avg)+1)
else:
    if int(avg)-avg<0.5:
        print(int(avg))
    else:
        print(int(avg)-1)
integer=sorted(integer)
print(integer[N//2])
current=[0,0]
mode=[current]
for i in integer:
    if current[0]==i:
        current[1]+=1
    else:
        if mode[0][1]<current[1]:
            mode=[current]
        elif mode[0][1]==current[1]:
            mode.append(current)
        current=[i, 1]
if mode[0][1]<current[1]:
    mode=[current]
elif mode[0][1]==current[1]:
    mode.append(current)
try:
    a=1
    while True:
        if mode[a]!=mode[0]:
            print(mode[a][0])
            break
        else:
            a+=1
except:
    print(mode[0][0])
print(integer[-1]-integer[0])