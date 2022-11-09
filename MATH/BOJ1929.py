# 소수 구하기

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# for i in range(m, n+1):
#     if i == 1:
#         continue
#     isPrime = True
#     for j in range(2, int(i**0.5)+1):
#         if i%j == 0:
#             isPrime = False
#             break
#     if isPrime:
#         print(i)

m, n = map(int, input().split())

prime = [False, False] + [True] * (n-1)

# for i in range(2, n):
for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False

for i in range(m, n+1):
    if prime[i]:
        print(i)

