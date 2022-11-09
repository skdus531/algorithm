# 숫자 카드
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
check = list(map(int, input().split()))

answer = []

# 이진탐색으로 풀이

# for c in check:
#     start, end = 0, n-1
#     exist = False
#     while start <= end:
#         mid = (start + end) // 2
#         if cards[mid] == c:
#             exist = True
#             break
#         elif cards[mid] < c:
#             start = mid + 1
#         else:
#             end = mid - 1
#     if exist:
#         answer.append(1)
#         continue
#     answer.append(0)    

# for i in answer:
#     print(i, end=' ')


# Dictionary 로 풀이

dic = {}
for card in cards:
    dic[card] = 1
for c in check:
    if c in dic:
        answer.append(1)
    else:
        answer.append(0)

for i in answer:
    print(i, end=' ')