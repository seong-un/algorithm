string=input()
alphabet=[-1]*26
for i in range(97, 123):
    if chr(i) in string:
        alphabet[i-97]=string.index(chr(i))
print(*alphabet)