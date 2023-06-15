len_stair = int(input())

stairs = [int(input()) for i in range(len_stair)]

if len_stair >= 3:
    dp = [stairs[0], stairs[0] + stairs[1], max(stairs[0], stairs[1]) + stairs[2]]
    for i in range(3, len_stair):
        dp.append(stairs[i] + max(dp[i-2], dp[i-3] + stairs[i-1]))

    print(dp[-1])
else:
    print(sum(stairs))