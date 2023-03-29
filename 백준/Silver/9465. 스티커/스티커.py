T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    sticker=[list(map(int, input().split())) for i in range(2)]
    if n>1:
        sticker[0][1]=sticker[1][0]+sticker[0][1]
        sticker[1][1]=sticker[0][0]+sticker[1][1]
        for i in range(2, n):
            sticker[0][i]=max(sticker[1][i-2], sticker[1][i-1])+sticker[0][i]
            sticker[1][i]=max(sticker[0][i-2], sticker[0][i-1])+sticker[1][i]
        print(max(sticker[0][-1], sticker[1][-1]))
    else:
        print(*max(sticker))