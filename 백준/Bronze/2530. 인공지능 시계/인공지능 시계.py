A, B, C = map(int, input().split())
C += int(input())

if C >= 60:
    B += C // 60
    C %= 60
    if B >= 60:
        A += B // 60
        B %= 60
        if A >= 24:
            A %= 24

print(A, B, C, sep=" ")