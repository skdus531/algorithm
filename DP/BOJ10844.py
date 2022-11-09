# 쉬운 계단 수
import sys
input = sys.stdin.readline

n = int(input())
cnt = [0,1,1,1,1,1,1,1,1,1]
for i in range(n-1):
    new_cnt = []
    new_cnt.append(cnt[1])
    for j in range(1,9):
        new_cnt.append(cnt[j-1]+cnt[j+1])
    new_cnt.append(cnt[8])
    cnt = new_cnt
print(sum(cnt)%1000000000)
