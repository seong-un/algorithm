string = input()
result = 0
for i in string:
    if i in ('a', 'e', 'i', 'o', 'u'):
        result += 1
print(result)