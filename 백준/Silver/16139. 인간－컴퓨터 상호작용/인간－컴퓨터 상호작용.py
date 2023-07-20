S = input()
Q = int(input())
alphabet = [[0] * (len(S) + 1) for i in range(26)]
for i in range(26):
    for j in range(len(S)):
        if chr(i + 97) == S[j]:
            alphabet[i][j+1] = alphabet[i][j] + 1
        else:
            alphabet[i][j+1] = alphabet[i][j]

for q in range(Q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    print(alphabet[ord(a) - 97][r + 1] - alphabet[ord(a) - 97][l])