T = int(input())
for test in range(T):
    d = int(input())
    t = 0
    while True:
        if t + t**2 <= d:
            t += 1
        else:
            print(t-1)
            break