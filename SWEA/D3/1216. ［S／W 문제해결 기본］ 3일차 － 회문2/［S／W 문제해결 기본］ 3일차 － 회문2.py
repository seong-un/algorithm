for _ in range(10):
    test_case=int(input())
    keyboard = [0] * 100
    for i in range(100):
        keyboard[i] = input()

    for_break=0
    length=100
    while length>0:
        for s in keyboard:
            for i in range(100 - length + 1):
                if s[i:i + length] == ''.join(list(reversed(s[i:i + length]))):
                    print(f'#{test_case} {length}')
                    for_break=1
                    break
            if for_break==1:
                break
        if for_break==1:
            break

        for s in list(zip(*keyboard)):
            for i in range(100 - length + 1):
                if list(s)[i:i + length] == list(reversed(list(s)[i:i + length])):
                    print(f'#{test_case} {length}')
                    for_break=1
                    break
            if for_break==1:
                break
        if for_break==1:
            break
        length-=1