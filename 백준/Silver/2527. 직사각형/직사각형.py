for _ in range(4):
    square=list(map(int, input().split()))
    if square[0]<square[2]<square[4]<square[6] or square[6]<square[4]<square[2]<square[0] or square[1]<square[3]<square[5]<square[7] or square[7]<square[5]<square[3]<square[1] or square[3]<square[1]<square[7]<square[5] or square[5]<square[7]<square[1]<square[3] or square[2]<square[0]<square[6]<square[4] or square[4]<square[6]<square[0]<square[2]:
        print('d')
    elif square[0]<square[2]==square[4]<square[6] or square[4]<square[6]==square[0]<square[2]:
        if square[1]<square[3]==square[5]<square[7] or square[5]<square[7]==square[1]<square[3]:
            print('c')
        else:
            print('b')
    elif square[0]<square[4]<square[2]<square[6] or square[0]<square[4]<square[6]<square[2] or square[4]<square[0]<square[6]<square[2]:
        if square[1]<square[3]==square[5]<square[7] or square[5]<square[7]==square[1]<square[3]:
            print('b')
        else:
            print('a')
    else:
        if square[1]<square[3]==square[5]<square[7] or square[5]<square[7]==square[1]<square[3]:
            print('b')
        else:
            print('a')