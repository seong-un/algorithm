hexa=input()
decimal=0
i=0
for str in reversed(hexa):
    if str=='A':
        str=10
    elif str=='B':
        str=11
    elif str=='C':
        str=12
    elif str=='D':
        str=13
    elif str=='E':
        str=14
    elif str=='F':
        str=15
    decimal+=int(str)*16**i
    i+=1

print(decimal)