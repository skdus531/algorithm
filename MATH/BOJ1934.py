# 최소 공배수
import sys
input = sys.stdin.readline

n = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

for _ in range(n):
    n1, n2 = map(int, input().split())
    gcd_val = gcd(n1, n2)
    print(n1 * n2 // gcd_val)
