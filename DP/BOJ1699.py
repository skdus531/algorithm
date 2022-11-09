# 제곱 수의 합
import sys
input = sys.stdin.readline

n = int(input())
dp = [0,1,2,3]
cnt = 2
for i in range(4,n+1):
    if i == cnt**2:
        dp.append(1)
        cnt += 1
    else: dp.append(dp[-1]+1)
for i in range(8,n+1):
    j = 2
    while j**2 <= i:
        dp[i] = min(dp[i],dp[i-j**2]+1)
        j += 1
print(dp[n])