A, B, C=map(int, input().split())

def power(A, B,C):
    if B==1:
        return A%C
    if B%2==1:
        return power(A, B//2,C)**2*A%C
    else:
        return power(A, B//2,C)**2%C

print(power(A, B,C))