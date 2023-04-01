N=int(input())
number=list(map(int, input().split()))
not_prime_number=set()
prime_number=set(i for i in range(2, 1001))
for i in range(2, 501):
    for j in range(2*i, 1001, i):
        not_prime_number.add(j)
prime_number=prime_number-not_prime_number
cnt=0
for i in number:
    if i in prime_number:
        cnt+=1
print(cnt)