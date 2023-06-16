import sys
input=sys.stdin.readline

N = int(input())
M = int(input())
S = input()

PN = "IO" * N + "I"
PN_length = len(PN)
result = 0
for i in range(M):
    if PN == S[i:i+PN_length]:
        result += 1
print(result)