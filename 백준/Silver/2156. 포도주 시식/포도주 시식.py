n = int(input())

wine = [0] * n
for i in range(n):
    wine[i] = int(input())

max_wine = []
if n>2:
    max_wine.append(wine[0])
    max_wine.append(wine[0] + wine[1])
    max_wine.append(max(max(wine[0], wine[1]) + wine[2], max_wine[1]))
    for i in range(3, n):
        max_wine.append(max(max(max_wine[i-2], max_wine[i-3] + wine[i-1]) + wine[i], max_wine[-1]))
    print(max_wine[-1])
else:
    print(sum(wine))