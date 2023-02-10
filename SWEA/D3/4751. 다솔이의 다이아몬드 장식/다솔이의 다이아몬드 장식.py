T=int(input())
for test_case in range(1, T+1):
    string=input()
    print('..#.'*len(string)+'.', '.#.#'*len(string)+'.', sep='\n')
    for i in string:
        print(f'#.{i}.', end='')
    print('#')
    print('.#.#'*len(string)+'.', '..#.'*len(string)+'.', sep='\n')