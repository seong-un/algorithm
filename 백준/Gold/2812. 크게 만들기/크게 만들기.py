N, K = map(int, input().split())
number = list(map(int, list(input())))

result = []
for i in range(len(number)):
    while True:
        if result and result[-1] < number[i] and K > 0:
            K -= 1
            result.pop()
        else:
            result.append(number[i])
            break
    if K == 0:
        result += number[i+1:]
        break
    if i == len(number) - 1 and K > 0:
        result = result[:-K]

print(int(''.join(map(str, result))))