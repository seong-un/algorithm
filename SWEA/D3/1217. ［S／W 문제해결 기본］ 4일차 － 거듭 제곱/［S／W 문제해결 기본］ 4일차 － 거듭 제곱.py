def 거듭제곱(num, cnt):
    if cnt == 1:
        return num
    return 거듭제곱(num, cnt - 1) * num


for t in range(1, 11):
    _ = input()
    num, cnt = map(int, input().split())
    print(f'#{t} {거듭제곱(num, cnt)}')
