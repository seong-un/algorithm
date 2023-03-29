T=int(input())
for test_case in range(1, T+1):
    binary=list(input())
    triad=list(input())
    set_binary=set()
    set_triad=set()
    for i in range(len(binary)):
        if binary[i]=='0':
            binary[i]='1'
        else:
            binary[i]='0'
        set_binary.add(int(''.join(binary),2))
        if binary[i]=='0':
            binary[i]='1'
        else:
            binary[i]='0'
    for i in range(len(triad)):
        if triad[i]=='0':
            triad[i]='1'
            set_triad.add(int(''.join(triad), 3))
            triad[i]='2'
            set_triad.add(int(''.join(triad), 3))
            triad[i]='0'
        elif triad[i]=='1':
            triad[i] = '2'
            set_triad.add(int(''.join(triad), 3))
            triad[i] = '0'
            set_triad.add(int(''.join(triad), 3))
            triad[i] = '1'
        else:
            triad[i] = '0'
            set_triad.add(int(''.join(triad), 3))
            triad[i] = '1'
            set_triad.add(int(''.join(triad), 3))
            triad[i] = '2'
    print(f'#{test_case}', *(set_binary & set_triad))