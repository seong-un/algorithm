horizon, vertex = map(int, input().split())
length = int(input())
store = [0] * length
for i in range(length):
    store[i] = list(map(int, input().split()))
dongeun = [list(map(int, input().split()))]
point=[0]*(length+1)
for idx, i in enumerate(store+dongeun):
    if i[0]==3:
        point[idx]=i[1]
    elif i[0]==2:
        point[idx]=vertex+i[1]
    elif i[0]==4:
        point[idx]=2*vertex+horizon-i[1]
    else:
        point[idx]=2*(vertex+horizon)-i[1]
result=0
for i in point[:length]:
    if abs(point[-1]-i)<2*(horizon+vertex)-abs(point[-1]-i):
        result+=abs(point[-1]-i)
    else:
        result+=2*(horizon+vertex)-abs(point[-1]-i)
print(result)