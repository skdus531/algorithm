# 카드

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

cards = []
for _ in range(n):
    card = int(input())
    cards.append(card)
cards.sort()

cntr = Counter(cards)
cntr.most_common()
print(list(cntr.most_common())[0][0])
