## 트리의 지름 (공식 알기)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, 0))
    while q:
        node, distance = q.popleft()
        dist[node] = distance
        for i in graph[node]:
            if i[0] == start or dist[i[0]]:
                continue
            q.append((i[0], i[1] + distance))

n = int(input())
graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(n-1):
    a, b, e = map(int, input().split())
    graph[a].append((b, e))
    graph[b].append((a, e))

dist = [0] * (n+1)
bfs(1)
farthest = 1   # 2로 해서 n = 1 일 때 indexError 떴음 항상 edge case 조심!
mx = -1
for i in range(2, n+1):
    if dist[i] > mx:
        farthest = i
        mx = dist[i]
    dist[i] = 0
bfs(farthest)

print(max(dist))
