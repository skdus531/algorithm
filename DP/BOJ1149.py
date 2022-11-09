# RGB 거리
import sys
input = sys.stdin.readline

cost = []
n = int(input())

for i in range(n):
	cost.append(list(map(int,input().split())))
	if i > 0:
		cost[i][0] += min(cost[i-1][1],cost[i-1][2])
		cost[i][1] += min(cost[i-1][0],cost[i-1][2])
		cost[i][2] += min(cost[i-1][1],cost[i-1][0])

print(min(cost[n-1]))