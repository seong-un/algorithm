A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

if A[0] == B[0]:
    print(C[0], end = " ")
elif A[0] == C[0]:
    print(B[0], end = " ")
else:
    print(A[0], end = " ")

if A[1] == B[1]:
    print(C[1])
elif A[1] == C[1]:
    print(B[1])
else:
    print(A[1])