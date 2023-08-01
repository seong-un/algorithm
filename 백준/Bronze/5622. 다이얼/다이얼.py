string = input()
result = 0
for i in string:
    if ord(i) <= 79:
        result += (ord(i) - 62) // 3 + 2
    elif ord(i) <= 83:
        result += 8
    elif ord(i) <= 86:
        result += 9
    elif ord(i) <= 90:
        result += 10
print(result)