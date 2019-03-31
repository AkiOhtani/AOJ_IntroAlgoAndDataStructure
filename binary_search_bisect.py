import sys
import bisect
input = sys.stdin.readline

n = int(input())
S = list(map(lambda x: int(x), input().strip().split()))

q = int(input())

count = 0
for t in input().strip().split():
    t = int(t)
    if S[bisect.bisect_left(S, t)] == t:
        count += 1
print(count)
