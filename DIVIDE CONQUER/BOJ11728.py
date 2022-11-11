# 배열 합치기

##  Merge Sort (Memory 많이 쓰는 ver)

# def merge_sort(lst):
#     if len(lst) < 2:
#         return lst

#     mid = len(lst) // 2

#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])

#     new_lst = []
#     p_left, p_right = 0, 0
#     while p_left < len(left) and p_right < len(right):
#         if left[p_left] < right[p_right]:
#             new_lst.append(left[p_left])
#             p_left += 1
#         else:
#             new_lst.append(right[p_right])
#             p_right += 1
#     new_lst += left[p_left:]
#     new_lst += right[p_right:]

#     return new_lst






import sys
input = sys.stdin.readline

## Merge Sort (Index ver)

def merge_sort(lst, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(lst, l, mid)
    merge_sort(lst, mid + 1, r)
    merge(lst, l, mid + 1, r)


def merge(lst, left, mid, right):
    new_lst = []
    l, r = left, mid

    while l < mid and r <= right:
        if lst[l] <= lst[r]:
            new_lst.append(lst[l])
            l += 1
        else:
            new_lst.append(lst[r])
            r += 1
    
    while l < mid:
        new_lst.append(lst[l])
        l += 1
    while r <= right:
        new_lst.append(lst[r])
        r += 1

    for i in range(len(new_lst)):
        lst[left] = new_lst[i]
        left += 1

n, m = map(int, input().split())

arr = list(map(int, input().split())) + list(map(int, input().split()))
merge_sort(arr, 0, len(arr)-1)
for i in sorted(arr):
    print(i, end=' ')