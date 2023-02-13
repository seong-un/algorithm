N=int(input())
series=list(map(int, input().split()))
ascend=1
descend=1
max_length=[]
for i in range(N-1):
    if series[i]<series[i+1]:
        ascend+=1
        if descend!=1:
            max_length.append(descend)
            descend=1
    elif series[i]>series[i+1]:
        descend+=1
        if ascend!=1:
            max_length.append(ascend)
            ascend=1
    else:
        ascend+=1
        descend+=1
max_length.append(ascend)
max_length.append(descend)
print(max(max_length))