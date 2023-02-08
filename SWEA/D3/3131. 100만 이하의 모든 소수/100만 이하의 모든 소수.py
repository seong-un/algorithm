prime_number=[1 for i in range(1000000)]
prime_number[0]=0
for i in range(2, 1000):
    prime_number[2*i-1::i]=[0]*(int(1000000/i)-1)
for idx, i in enumerate(prime_number):
    if i==1:
        print(idx+1, end=' ')