import sys
import math
input = sys.stdin.readline

T = int(input())
prime = [2]
a= prime[-1]
while prime[-1]<=math.sqrt(4*10**9):
    for i in prime:
        if a%i==0:
            break
        if i>math.sqrt(a):
            prime.append(a)
            break
    a+=1
for t in range(T):
    n=int(input())
    if n in [0, 1]:
        print(2)
        continue
    for_break=False
    while True:
        for j in prime:
            if j==n:
                print(n)
                for_break=True
                break
            if n%j==0:
                break
            if j==prime[-1]:
                print(n)
                for_break=True
                break
        if for_break:
            break
        n+=1