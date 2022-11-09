# 보석 도둑
# from bisect import bisect_left
import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

gems = []
for _ in range(n):
    m, v = map(int, input().split())
    gems.append([m, v])
gems.sort(reverse=True)

bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

answer = 0
rem = []
for bag in bags:
    while gems and gems[-1][0] <= bag:
        weight, value = gems.pop()
        heapq.heappush(rem, -value)
    if rem:
        answer -= heapq.heappop(rem)
print(answer)

# answer = 0
# num = 0
# for weight, value in gems:
#     if num == k:
#         break
#     idx = bisect_left(bags, weight)
#     if idx == k:
#         continue
#     if not isEmpty[idx]:
#         find = False
#         for i in range(idx+1, k):
#             if isEmpty[i]:
#                 idx = i
#                 find = True
#                 break
#         if not find:
#             continue
#     isEmpty[idx] = False
#     answer += value
#     num += 1
# print(answer)