S = input()
Q = int(input())
alphabet = [[0] * len(S) for i in range(26)]
for i in range(26):
    for j in range(len(S)):
        if chr(i + 97) == S[j]:
            if j == 0:
                alphabet[i][j] = 1
            else:
                alphabet[i][j] = alphabet[i][j-1] + 1
        else:
            if j == 0:
                alphabet[i][j] = 0
            else:
                alphabet[i][j] = alphabet[i][j-1]

for q in range(Q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    if l != 0:
        print(alphabet[ord(a) - 97][r] - alphabet[ord(a) - 97][l - 1])
    else:
        print(alphabet[ord(a) - 97][r])