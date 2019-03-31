import sys
input = sys.stdin.readline

M = 104627
L = 12

H = [[] * L] * M

def getChar(char):
    if char == "A":
        return 1
    elif char == "C":
        return 2
    elif char == "G":
        return 3
    elif char == "T":
        return 4
    else:
        return 0

def getKey(string):
    sum = 0
    p = 1
    for char in string:
        sum += p * getChar(char)
        p *= 5
    return sum

def h1(key):
    return key % M

def h2(key):
    return 1 + (key % (M - 1))

def find(string):
    global H
    key = getKey(string) # 文字列を数値に変換
    i = 0
    while 1:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == string:
            return 1
        elif len(H[h]) == 0:
            return 0
        i += 1
    return 0

def insert(string):
    global H
    key = getKey(string) # 文字列を数列に変換
    i = 0
    while 1:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == string:
            return 1
        elif len(H[h]) == 0:
            H[h] = string
            return 0
        i += 1
    return 0

N = int(input())

for i in range(N):
    line = input().strip().split()
    if line[0] == "insert":
        insert(line[1])
    elif line[0] == "find":
        if find(line[1]):
            print("yes")
        else:
            print("no")