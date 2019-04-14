import sys
input = sys.stdin.readline

class Node:
    child = {"" : None}

def setChild(node, c):
    node.child[c] = Node() 

class TrieTree:
    node = Node()

    def insert(self, key):
        node = self.node # 先頭のNodeのオブジェクト
        for c in key:
            if node.child.get(c) == None:
                setChild(node, c)
            node = node.child[c] # 子ノードに移動
        if node.child.get("\0") == None: # 末尾チェック用に"\0"をセット
            setChild(node, "\0")
        return True
    
    def find(self, key):
        node = self.node # 先頭のNodeのオブジェクト
        if not key: # keyが空文字列の場合
            print("検索文字列が空です")
            return False
        else: # ループケース
            for c in key:
                if node.child.get(c) == None: # 文字コードが配列キーとなる
                    print("Not Found")
                    return False
                node = node.child[c] # 子ノードに移動
            if node.child.get("\0"):
                print("Found")
                return True
            else:
                print("Not Found")
                return False

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