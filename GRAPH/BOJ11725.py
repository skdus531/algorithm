## 트리 부모 찾기 (재귀로 잘 했음)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def addParent(node):
    for i in tree[node]:
        if parent[i] != 0:
            continue
        parent[i] = node
        addParent(i)

n = int(input())
tree = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0, 1] + [0]*(n-1)
addParent(1)

for i in parent[2:]:
    print(i)