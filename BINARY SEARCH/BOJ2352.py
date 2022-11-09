# 반도체 설계

from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
semi = list(map(int, input().split()))

# dp = [1] * (N)

# for i in range(N):
#     for j in range(0, i):
#         if semi[j] < semi[i]:
#             dp[i] = max(dp[j]+1, dp[i])
# print(max(dp))

# -> 시간 초과

answer = [semi[0]]
for s in semi:
    if s > answer[-1]:
        answer.append(s)
    else:
        answer[bisect_left(answer, s)] = s
print(len(answer))