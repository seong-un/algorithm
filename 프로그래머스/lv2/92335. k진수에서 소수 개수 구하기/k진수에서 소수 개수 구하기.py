def solution(n, k):
    answer = 0
    prime = ''
    while n > 0:
        prime = str(n % k) + prime
        n = n // k
    for i in prime.split('0'):
        if i in ['', '1']:
            continue
        is_prime = True
        for j in range(2, int(int(i) ** 0.5 + 1)):
            if not int(i) % j:
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer