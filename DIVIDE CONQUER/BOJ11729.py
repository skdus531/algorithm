# 하노이의 탑

import sys
input = sys.stdin.readline

def hanoi(fr, to, mid, n):
    global answer
    if n == 1:
        answer += 1
        move.append((fr, to))
        return

    hanoi(fr, mid, to, n-1)
    hanoi(fr, to, mid, 1)
    hanoi(mid, to, fr, n-1)


N = int(input())
answer = 0
move = []
hanoi(1, 3, 2, N)

print(answer)
for f, t in move:
    print("%d %d"%(f, t))