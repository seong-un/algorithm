def turn_90(n,M):
    mat_90=[]
    for j in range(n):
        row=[]
        for i in range(n):
            row.append(M[n-i-1][j])
        mat_90.append(row)
    return mat_90

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    mat=[]
    for i in range(N):
        mat.append(list(input().split()))
    mat_90=turn_90(N, mat)
    mat_180=turn_90(N, mat_90)
    mat_270=turn_90(N, mat_180)
    print(f"#{test_case}")
    for i in range(N):
        print(''.join(mat_90[i]), ''.join(mat_180[i]), ''.join(mat_270[i]))