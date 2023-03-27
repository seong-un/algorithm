N, M=map(int, input().split())
chess=[list(input()) for _ in range(N)]
min_cnt=[]
for i in range(N-7):
    for j in range(M-7):
        cnt=0
        alpha=0
        for I in range(i, i+8):
            for J in range(j, j+8):
                if (I+J)%2==(i+j)%2:
                    if chess[I][J]!=chess[i][j]:
                        cnt+=1
                    else:
                        alpha+=1
                else:
                    if chess[I][J]==chess[i][j]:
                        cnt+=1
                    else:
                        alpha+=1
        min_cnt.extend([cnt, alpha])
print(min(min_cnt))