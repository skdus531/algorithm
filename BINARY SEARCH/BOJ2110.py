# 공유기 설치
from bisect import bisect_left
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

c -= 2
start, end = 1, houses[-1] - houses[0]
dist = 0
while start <= end:
    mid = (start + end) // 2
    prev = houses[0]
    dists = []
    for _ in range(c):
        next = prev + mid
        idx = bisect_left(houses, next)
        if idx >= n-1:
            break
        next = houses[idx]
        dists.append(next-prev)
        prev = next
    
    if len(dists) == c:
        dists.append(houses[-1] - prev)
        mn = min(dists)
        if mn < mid:
            end = mid -1
            continue
        dist = max(dist, mn)
        start = mid + 1
    else:
        end = mid - 1
print(dist)
