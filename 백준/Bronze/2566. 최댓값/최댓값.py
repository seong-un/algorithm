max_num=[0,0,0]
for i in range(9):
    matrix=list(map(int, input().split()))
    if max(matrix)>max_num[0]:
        max_num=[max(matrix), i, matrix.index(max(matrix))]
print(max_num[0])
print(max_num[1]+1, max_num[2]+1)