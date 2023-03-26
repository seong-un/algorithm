N=int(input())
room=1
N-=1
bee=6
while N>0:
    N-=bee
    bee+=6
    room+=1
print(room)