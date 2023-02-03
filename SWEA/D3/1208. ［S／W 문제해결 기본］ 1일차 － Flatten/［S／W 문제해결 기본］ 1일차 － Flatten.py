for test_case in range(1, 11):
    dump=int(input())
    boxes=list(map(int, input().split()))
    for i in range(dump):
        boxes[boxes.index(max(boxes))]-=1
        boxes[boxes.index(min(boxes))]+=1
    print(f'#{test_case} {max(boxes)-min(boxes)}')