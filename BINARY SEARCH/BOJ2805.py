# 나무 자르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
height = 0
while start <= end:
    
    mid = (start + end) // 2
    cut_tree = 0
    for tree in trees:
        cut = tree - mid
        if cut > 0:
            cut_tree += cut
    if cut_tree >= m:
        height = max(height, mid)
        start = mid + 1
    else:
        end = mid - 1
print(height)