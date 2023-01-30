import copy

for i in range(10):
    test_case=int(input())
    maze=[]
    for i in range(100):
        maze.append(list(map(int, input())))
    count=0
    for i in range(100):
        for j in range(100):
            count+=1
            if maze[i][j]==2:
                a=i;b=j
    vst=[[a,b]]
    visiting=[]
    while True:
        for i in vst:
            if maze[i[0]+1][i[1]] in [0,3]:
                visiting.append([i[0]+1, i[1]])
                maze[i[0]+1][i[1]]=2
            if maze[i[0]-1][i[1]] in [0,3]:
                visiting.append([i[0]-1, i[1]])
                maze[i[0]-1][i[1]]=2
            if maze[i[0]][i[1]+1] in [0,3]:
                visiting.append([i[0], i[1]+1])
                maze[i[0]][i[1]+1]=2
            if maze[i[0]][i[1]-1] in [0,3]:
                visiting.append([i[0], i[1]-1])
                maze[i[0]][i[1]-1]=2
        vst=copy.deepcopy(visiting)
        visiting=[]
        if not vst:
            break
    printing=1
    for i in range(100):
        if 3 in maze[i]:
            printing=0
    print(f'#{test_case} {printing}')