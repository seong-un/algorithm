import math

N, K= map(int, input().split())
students=[[0, 0] for i in range(7)]
for i in range(N):
    S, Y=map(int, input().split())
    students[Y][S]+=1
room=0
for i in students:
    room+=math.ceil(i[0]/2)+math.ceil(i[1]/2)
print(room)