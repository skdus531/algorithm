# 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
grape = [0]
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    grape.append(int(input()))
    if i == 1 : dp[i] = grape[i]
    elif i == 2 : dp[i] = grape[i] + grape[i-1]
    else: dp[i] = max(dp[i-1],dp[i-2]+grape[i],dp[i-3]+grape[i-1]+grape[i])
print(dp[n])
