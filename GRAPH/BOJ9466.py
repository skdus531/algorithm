# 텀 프로젝트 
# 반복문으로 할 수도! 
# next 타고 들어가면서 vertex 저장하면 굳이 visited, team 따로 안 둬도 ok

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

init = 0
def DFS(vertex):
    global init
    visited[vertex] = True
    s = graph[vertex]
    if s == vertex:
        team[s] = 1
        return False
    if visited[s]:
        if team[s]>-1:
            team[vertex] = 0
            return False
        else:
            team[vertex] = 1
            init = s
            return True
    elif not DFS(s):
        team[vertex] = 0
        return False
    else: 
        team[vertex] = 1
        if vertex==init:
            return False
        return True
      
T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0]+list(map(int,input().split()))
    team = [-1]*(n+1)
    visited = [False]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            init = i
            DFS(i)
    ans = 0
    for i in team[1:]:
        if not i: ans +=1
    print(ans)