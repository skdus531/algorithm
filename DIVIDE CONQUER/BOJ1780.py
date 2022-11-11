# 종이의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def split(x, y, n):
    val = paper[x][y]

    if n == 1:
        answer[val+1] += 1
        return

    same = True
    for i in range(n):
        if not same:
            break
        for j in range(n):
            if paper[x+i][y+j] != val:
                same = False
                break
    
    if not same:
        n //= 3
        for i in range(3):
            for j in range(3):
                split(x+i*n, y+j*n, n)
    else:
        answer[val+1] += 1



N = int(input())
answer = [0, 0, 0]
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
split(0, 0, N)

for i in answer:
    print(i)
