## 다리 만들기
from collections import deque
import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    imap[x][y] = -inum

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >=n:
            continue
        
        if imap[nx][ny] == 1:
            dfs(nx, ny)


def bfs(island):
    global answer
    dist = [[-1]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if imap[i][j] == island:
                dist[i][j] = 0
                q.append((i, j))

    while True:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if dist[nx][ny] != -1:  # 어차피 bfs라서 최솟값 갱신 안됨. 방문했으면 그게 최소
                continue

            if imap[nx][ny] < 0 and imap[nx][ny] != island:
                answer = min(answer, dist[x][y])
                return
            
            if imap[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


n = int(input())
imap = [[] for _ in range(n)]
for i in range(n):
    imap[i] = list(map(int, input().split()))

inum = 1
for i in range(n):
    for j in range(n):
        if imap[i][j] == 1:
            dfs(i, j)
            inum += 1
answer = 10**9  # 최대를 n으로 잡아서 계속 틀렸음;; 걍 max 값으로 해주자

for i in range(1, inum):
    bfs(-i)

print(answer)