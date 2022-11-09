# 스티커

import copy
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    dp = copy.deepcopy(sticker)
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) 
        dp[1][i] += max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
    print(max(dp[0][n-1], dp[1][n-1], dp[0][n-2], dp[1][n-2]))