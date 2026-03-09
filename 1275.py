from sys import stdin

N = Q = None

arr = tree = querys = []

read_val = list(map(int, stdin.readline().strip().split()))

def input_val() : # 
    global N, Q, arr, tree, querys

    N, Q = read_val

    tree = [0] * N * 4
    
    arr = [0]
    arr.extend(read_val)

    querys = [read_val for _ in range(Q)]

def build(node, start, end) :
    if start == end :
        tree[start] = arr[start]
        return
    
    mid = (start + end) / 2

    tree[node] = build(node, start, mid) + 
       

def update(node, start, end, index, val) :

def query(node, start, end, left, right) :

def solution() :
    global N, Q, arr, tree, querys

    build(1, 1, N)

    

if __name__ == "__main__" :
    solution()