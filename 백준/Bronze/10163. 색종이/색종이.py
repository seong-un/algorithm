N = int(input())
colored_paper = [0] * N
for i in range(N):
    colored_paper[i] = list(map(int, input().split()))
horizon, vertex=0,0
for i in range(N):
    if horizon<colored_paper[i][1]+colored_paper[i][3]:
        horizon=colored_paper[i][1]+colored_paper[i][3]
for i in range(N):
    if vertex<colored_paper[i][0]+colored_paper[i][2]:
        vertex=colored_paper[i][0]+colored_paper[i][2]
plane = [[0] * (horizon) for _ in range(vertex)]
for i in range(1, N + 1):
    for j in range(colored_paper[i - 1][0], colored_paper[i - 1][0] + colored_paper[i - 1][2]):
        plane[j][colored_paper[i - 1][1]:colored_paper[i - 1][1] + colored_paper[i - 1][3]] = [i] * (
            colored_paper[i - 1][3])
numbers = [0] * N
for i in plane:
    for j in i:
        for k in range(N):
            if j == k + 1:
                numbers[k] += 1
for i in numbers:
    print(i)