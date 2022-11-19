# 정점들의 거리
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v, t, n):
    dist = [-1] * (n+1)
    q = deque()
    q.append((v, 0))

    while q:
        vertex, d = q.popleft()
        dist[vertex] = d

        for nxt, nd in tree[vertex]:
            if nxt == t:
                print(d+nd)
                return

            if dist[nxt] == -1:
                q.append((nxt, d+nd))

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    v1, v2, d = map(int, input().split())
    tree[v1].append((v2, d))
    tree[v2].append((v1, d))

M = int(input())

for _ in range(M):
    v1, v2 = map(int, input().split())
    bfs(v1, v2, N)