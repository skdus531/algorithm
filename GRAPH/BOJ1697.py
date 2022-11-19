## 숨바꼭질
from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, k):
    if n == k:
        print(0)
        return
    
    dist = {}
    q = deque([])
    q.append((n, 0))

    while q:
        point, cnt = q.popleft()

        dist[point] = cnt

        for m in [1, -1, point]:
            nxt = point + m
            
            if nxt == K:
                print(cnt+1)
                return
            if nxt < 0 or nxt > 100000:
                continue
            if dist.get(nxt, 10**6) <= cnt + 1:
                continue
            q.append((nxt, cnt + 1))


N, K = map(int, input().split())
bfs(N, K)