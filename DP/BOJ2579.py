# 계단오르기

import sys
input = sys.stdin.readline
n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [0] + stairs
if n > 1:
    dp[2] += dp[1]
    for i in range(3, n+1):
        dp[i] += max(stairs[i-2]+dp[i-3], dp[i-2])
print(dp[-1])