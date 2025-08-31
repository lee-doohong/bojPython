import sys

class Node :
    def __init__(self, value) :
        self.value = value
        self.childs = []

    def add_child(self, Node) :
        self.childs.append(Node)

def dfs(Node) :
    result = 0
    if not Node.childs :
        result += 1
    else : 
        for i in Node.childs :
            result += dfs(i)
    return result

def main() :
    root = None

    N = int(input())

    parent = list(map(int, sys.stdin.readline().split()))

    remove_Node = int(input())

    nodes = [Node(i) for i in range(N)]

    for i, p in enumerate(parent) : 
        if p == -1 : 
            root = nodes[i]
        else : 
            nodes[p].add_child(nodes[i])

    print(dfs(root) - dfs(nodes[remove_Node]) + (1 if len(nodes[parent[remove_Node]].childs) == 1 else 0))
    
if __name__ == "__main__" :
    main()