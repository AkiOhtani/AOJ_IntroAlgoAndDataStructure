import sys
input = sys.stdin.readline

n = int(input())
S = input().strip().split()

q = int(input())
T = input().strip().split()
count = 0
for i in range(q):
    S.append(T[i])
    j = 0
    while S[j] != T[i]:
        j += 1
    if j != len(S[:-1]):
        count += 1
    S = S[:-1]
print(count)