rest=set()
for i in range(10):
    divide=int(input())
    rest.add(divide%42)
print(len(rest))