import sys
input = sys.stdin.readline

class Node:
    child = {"" : None}
    def setChild(self, c):
        self.child[c] = Node() 

###############################################################################
### @ref : https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A9%E3%82%A4%E6%9C%A8
###############################################################################
class TrieTree:
    node = Node()

    def insert(self, key):
        node = self.node # 先頭のNodeのオブジェクト
        for c in key:
            child = node.child.get(c) # 文字コードが配列キーとなる
            if child == None:
                node.setChild(c)
            node = node.child[c] # 子ノードに移動
        return True
    
    def find(self, key):
        node = self.node # 先頭のNodeのオブジェクト
        if not key: # keyが空文字列の場合
            "検索文字列が空です"
            return False
        else: # ループケース
            for c in key:
                child = node.child.get(c) # 文字コードが配列キーとなる
                if child == None:
                    print("Not Found")
                    return False
                node = node.child[c] # 子ノードに移動
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