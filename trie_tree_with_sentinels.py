import sys
input = sys.stdin.readline

class Node:
    value = None
    child = {"" : None}
    def __init__(self, value):
        self.value = value

    def setChild(self, c):
        self.child[c] = Node(c) 

null = Node(None)
#null.child = null

###############################################################################
### @ref : https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A9%E3%82%A4%E6%9C%A8
###############################################################################
class TrieTree:
    global null # 番兵Node
    node = null

    def insert(self, key):
        node = self.node # 先頭のNodeのオブジェクト
        key += "\0" # 番兵char
        index = 0
        while key[index] != "\0":
            c = key[index] # keyが空でないので1文字目を取り出す
            child = node.child.get(c) # 文字コードが配列キーとなる
            if child == None:
                node.setChild(c)
            node = node.child[c] # 子ノードに移動
            index += 1
        return True
    
    def find(self, key):
        node = self.node # 先頭のNodeのオブジェクト
        if not key: # keyが空文字列の場合
            print("検索文字列が空です")
            return False
        else: # ループケース
            key += "\0" # 番兵char
            index = 0
            while key[index] != "\0":
                c = key[index] # keyが空でないので1文字目を取り出す
                child = node.child.get(c) # 文字コードが配列キーとなる
                if child == None:
                    print("Not Found")
                    return False
                node = node.child[c] # 子ノードに移動
                index += 1
            print("Found")
            return True

def main():
    N = int(input())
    tree = TrieTree()
    for i in range(N):
        line = input().strip().split()
        if line[0] == "insert":
            tree.insert(line[1])
        elif line[0] == "find":
            tree.find(line[1])

if __name__ == "__main__":
    main()