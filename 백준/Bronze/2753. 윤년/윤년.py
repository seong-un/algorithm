year=int(input())
if not year%400:
    print(1)
elif not year%100:
    print(0)
elif not year%4:
    print(1)
else:
    print(0)