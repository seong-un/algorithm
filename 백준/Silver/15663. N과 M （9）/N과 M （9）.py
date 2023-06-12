from itertools import permutations

N, M = map(int, input().split())
array = list(map(int, input().split()))

MCN = sorted(set(permutations(array, M)))
for mcn in MCN:
    print(*mcn)