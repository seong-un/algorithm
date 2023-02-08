square=[[0]*4 for i in range(4)]
for i in range(4):
    square[i]=list(map(int, input().split()))
coordinate=set()
for i in square:
    for j in range(i[0], i[2]):
        for k in range(i[1], i[3]):
            coordinate.add((j,k))
print(len(coordinate))