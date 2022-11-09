# 최소 공배수

import sys

a, b = map(int, sys.stdin.readline().split())

if a < b:
    a, b = b, a
while b:
    a, b = b, a%b
print('1'*a)