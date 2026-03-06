from sys import stdin
from sys import maxsize

N = M = arr = querys = None
tree = None

def input_val() :
    global N, M, arr, querys, tree

    N, M = list(map(int, stdin.readline().strip().split()))

    arr = [-1]
    for _ in range(N) :
        arr.append(int(input()))

    querys = [list(map(int, stdin.readline().strip().split())) for _ in range(M)]
    tree = [0] * N * 4
    

def build(node, start, end):
    global N, M, arr, tree
    if start == end :
        tree[node] = arr[start]
        return tree[node]
    
    mid = int((start + end) / 2)
    
    tree[node] = min(build(node * 2, start, mid), build(node * 2 + 1, mid + 1, end))
    return tree[node]

def query(node, start, end, left, right) :
    global tree
    
    # 완전히 겹치지 않는 경우에는 0 반환
    if end < left or right < start :
        return maxsize
    # left와 right가 완전히 범위 안에 있는 경우에는 값 반환
    if left <= start and end <= right:
        return tree[node]
    
    mid = int((start + end) / 2)
    # 범위가 걸쳐 있는 경우에는 내림

    return min(query(node * 2, start, mid, left, right),  query(node * 2 + 1, mid + 1, end, left, right))

def solution() : 
    global querys, N, M, tree
    
    input_val()
    build(1, 1, N)

    results = []
    for i in querys : 
        results.append(str(query(1, 1, N, i[0], i[1])))
    print("\n".join(results).strip())

if __name__ == "__main__" :
    solution()