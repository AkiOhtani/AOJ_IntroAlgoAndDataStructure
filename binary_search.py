import sys
input = sys.stdin.readline

def binarySearch(slist, length, target):
    if length == 0:
        return 0
    even_flag = not(length % 2) # 偶数判定
    length = length // 2
    if slist[length] == target:
        return 1
    # 元のlengthが偶数長だったとき
    elif even_flag and slist[length - even_flag] == target:
        return 1
    elif slist[length] < target:
        return binarySearch(slist[length + 1:], length - even_flag, target)
    else:
        return binarySearch(slist[:length - even_flag], length - even_flag, target)
    return 0

def binarySearch2(A, n, key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return 0

n = int(input())
S = input().strip().split()
S = list(map(lambda x: int(x), S))

q = int(input())
#count = 0

#count = sum(list(map(lambda i: binarySearch2(S, n, T[i]), range(q))))
#for t in input().strip().split():
#    count += binarySearch(S, n, int(t))
print(sum(map(lambda t: binarySearch(S, n, int(t)), input().strip().split())))
