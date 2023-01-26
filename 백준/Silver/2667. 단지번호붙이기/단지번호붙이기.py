import copy

N=int(input())
house=[]
for _ in range(N):
    house.append(list(input()))
count=0
house_count_list=[]
for i in range(N):
    for j in range(N):
        if house[i][j]=='1':
            count+=1
            vst=[[i,j]]
            list(house)[i][j]='0'
            house_count=1
            while True:
                visiting=copy.deepcopy(vst)
                vst=[]
                for k in visiting:
                    if k[0]+1<=N-1:
                        if house[k[0]+1][k[1]]=='1':
                            house[k[0]+1][k[1]]='0'
                            house_count+=1
                            vst.append([k[0]+1,k[1]])
                    if k[0]-1>=0:
                        if house[k[0]-1][k[1]]=='1':
                            house[k[0]-1][k[1]]='0'
                            house_count+=1
                            vst.append([k[0]-1,k[1]])
                    if k[1]-1>=0:
                        if house[k[0]][k[1]-1]=='1':
                            house[k[0]][k[1]-1]='0'
                            house_count+=1
                            vst.append([k[0],k[1]-1])
                    if k[1]+1<=N-1:
                        if house[k[0]][k[1]+1]=='1':
                            house[k[0]][k[1]+1]='0'
                            house_count+=1
                            vst.append([k[0],k[1]+1])
                if not vst:
                    house_count_list.append(house_count)
                    break
print(count)
for i in sorted(house_count_list):
    print(i)