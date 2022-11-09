# 이분 그래프
from collections import deque
import sys
input = sys.stdin.readline


# def bfs(vertex):
#     q = deque()
#     q.append([vertex, 0])
#     while q:
#         v, t = q.popleft()
#         team[v] = t
#         if v not in graph:
#             continue
#         for i in graph[v]:
#             if team[i] == -1:
#                 q.append([i, 1-t])
#             elif team[i] == t:
#                 return False
#     return True

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(vertex):
    if team[vertex] == -1:
        team[vertex] = 0
    t = team[vertex]

    if vertex not in graph:
        return True
    
    for i in graph[vertex]:
        if team[i] == -1:
            team[i] = 1 - t
            if not dfs(i):
                return False
        elif team[i] == t:
            return False
    return True


T = int(input())
for _ in range(T):
    graph = {}
    v, e = map(int, input().split())
    for i in range(e):
        a, b = map(int, input().split())
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    team = [-1] * (v+1)
    
    flag = True
    for i in range(1, v+1):
        if team[i] == -1:
            if not dfs(i):
                flag = False
                break
    if not flag:
        print("NO")
    else:
        print("YES")