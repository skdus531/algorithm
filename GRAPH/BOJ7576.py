# 토마토
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append([i, j, 0])
    day = 0
    while q:
        x, y, d = q.popleft()
        day = d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    q.append([nx, ny, d+1])
                    box[nx][ny] = 1
    return day    

m, n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))

answer = bfs()
all = True
for i in range(n):
    if 0 in box[i]:
        all = False
answer = -1 if not all else answer
print(answer)