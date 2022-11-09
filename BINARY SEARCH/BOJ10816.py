# 숫자카드 2

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

dic = {}
for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for c in check:
    if c in dic:
        print(dic[c], end=' ')
    else:
        print(0, end=' ')