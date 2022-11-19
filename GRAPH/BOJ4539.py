# 이진 검색 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v = []
while True:
    try:
        v.append(int(input()))
    except:
        break

## index를 넘겨주는 방식으로

def post(st, end):
    if st > end:
        return

    root = v[st]

    cut = end + 1
    for i in range(st+1, end+1):
        if v[i] > root:
            cut = i
            break

    post(st+1, cut-1)
    post(cut, end)
    print(root)

post(0, len(v)-1)

## pre => post 로 바로 재귀로 출력 (배열 값을 그대로 넘겨줘서 메모리 많이 씀)

# def post(pre):
#     if len(pre) == 1:
#         print(pre[0])
#         return

#     root = pre[0]

#     cut = len(pre)
#     for i in range(1, len(pre)):
#         if pre[i] > root:
#             cut = i
#             break

#     left = pre[1:cut]
#     right = pre[cut:]
#     if left:
#         post(left)
#     if right:
#         post(right)
#     print(root)








## 트리 만들고 후위순회 O(NM) 시간초과

# def addChild(p, child):
#     if child < p:
#         if tree[p][0] == -1:
#             tree[p][0] = child
#             return
#         addChild(tree[p][0], child)
#     else:
#         if tree[p][1] == -1:
#             tree[p][1] = child
#             return
#         addChild(tree[p][1], child)

# def postorder(v):
#     if v not in tree:
#         return
#     postorder(tree[v][0])
#     postorder(tree[v][1])
#     print(v)


# root = int(input())
# tree = {root:[-1, -1]}
# while True:
#     try:
#         n = int(input())
#         tree[n] = [-1, -1]
#         addChild(root, n)
#     except:
#         break

# postorder(root)
