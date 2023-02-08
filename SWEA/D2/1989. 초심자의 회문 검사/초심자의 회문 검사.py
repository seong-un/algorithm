T=int(input())
for test_case in range(1, T+1):
    string=input()
    rev_string=list(string)
    rev_string.reverse()
    rev_string=''.join(rev_string)
    if rev_string==string:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')