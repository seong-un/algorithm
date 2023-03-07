H, W=map(int, input().split())
cloud=[0]*H
for i in range(H):
    cloud[i]=input()
weather=[[-1]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        move=0
        while j-move>=0:
            if cloud[i][j-move]=='c':
                weather[i][j]=move
                break
            else:
                move+=1
for i in weather:
    print(*i)