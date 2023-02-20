N=int(input())
for i in range(1, N+1):
    number=list(str(i))
    if '3' in number or '6' in number or '9' in number:
        print('-'*(number.count('3')+number.count('6')+number.count('9')), end=' ')
    else:
        print(i, end=' ')