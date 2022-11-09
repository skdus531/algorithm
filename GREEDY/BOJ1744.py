# 수 묶기 (반례 잘 생각)

import sys
input = sys.stdin.readline

N = int(input())

zero = 0
answer = 0
neg, pos = [], []
for _ in range(N):
    n = int(input())
    if n < 0:
        neg.append(n)
    elif n == 0:
        zero += 1
    else:
        if n == 1:
            answer += 1
            continue
        pos.append(n)
neg.sort()
pos.sort(reverse=True)


if len(neg) % 2 == 0:
    for i in range(0, len(neg)-1, 2):
        answer += neg[i] * neg[i+1]
else:
    for i in range(0, len(neg)-2, 2):
        answer += neg[i] * neg[i+1]
    if zero == 0:
        answer += neg[-1]

if len(pos) % 2 == 0:
    for i in range(0, len(pos)-1,2):
        answer += pos[i] * pos[i+1]
else:
    for i in range(0, len(pos)-2, 2):
        answer += pos[i] * pos[i+1]
    answer += pos[-1]
print(answer)