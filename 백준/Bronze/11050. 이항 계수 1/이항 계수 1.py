from itertools import combinations

N, K=map(int, input().split())
print(len(list(combinations([i for i in range(N)], K))))