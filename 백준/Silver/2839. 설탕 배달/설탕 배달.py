N = int(input())
bag = N//5
N = N%5
while bag>=0:
    if N%3:
        bag -= 1
        N += 5
    else:
        print(bag + N//3)
        break
if bag<0:
    print(-1)