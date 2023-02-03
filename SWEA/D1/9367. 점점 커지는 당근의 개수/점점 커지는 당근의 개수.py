T=int(input())
for test_case in range(1, T+1):
    len_carrot=int(input())
    carrot_size=list(map(int, input().split()))
    max_len_carrot=1
    current_len_carrot=1
    for i in range(len_carrot-1):
        if carrot_size[i]<carrot_size[i+1]:
            current_len_carrot+=1
        else:
            if max_len_carrot<current_len_carrot:
                max_len_carrot=current_len_carrot
            current_len_carrot=1
    print(f'#{test_case} {max(current_len_carrot, max_len_carrot)}')