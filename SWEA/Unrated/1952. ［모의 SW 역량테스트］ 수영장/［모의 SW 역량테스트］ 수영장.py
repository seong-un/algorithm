T = int(input())
for test_case in range(1, T + 1):
    day, month, mon3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 12

    dp[0] = min(plan[0] * day, month, mon3)
    dp[1]=min((plan[0]+plan[1])*day, min([plan[0], plan[1]])*day+month, month*2, mon3)
    dp[2]=min((plan[0]+plan[1]+plan[2])*day, min([plan[0], plan[1], plan[2]])*day+month*2, min([plan[0]+plan[1], plan[0]+plan[2], plan[1]+plan[2]])*day+month, month*3, mon3)

    for i in range(3, 12):
        dp[i] = min(dp[i - 1] + plan[i] * day, dp[i - 1] + month, dp[i - 3] + mon3)

    print(f'#{test_case} {min(dp[-1], year)}')
