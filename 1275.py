from sys import stdin

N = Q = None

arr = tree = querys = []

def read_val() :
    return list(map(int, stdin.readline().strip().split()))

def input_val() : # 
    global N, Q, arr, tree, querys

    N, Q = read_val()

    tree = [0] * N * 4
    
    arr = [0]
    arr.extend(read_val())
    # print(f" arr : {arr}")

    querys = [read_val() for _ in range(Q)]

def build(node, start, end) :
    # print(f"node : {node}, start : {start}, end : {end}")
    if start == end : # 두개가 붙었을때?
        tree[node] = arr[start]
        return tree[node]

    mid = int((start + end) / 2)

    tree[node] = build(node * 2, start, mid) + build(node * 2 + 1, mid + 1, end)
    return tree[node]

def update(node, start, end, index, val) :
    if index < start or end < index : # 범위 벗어난 경우 ? 제거
        return
    
    if start == end : # 리프노드 까지 내려갔다는 의미
        tree[node] = val
        return

    mid = int((start + end) / 2)
    
    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)

    tree[node] = tree[node * 2 + 1] + tree[node * 2]

def query(node, start, end, left, right) :
    
    if right < start or end < left : 
        return 0
    
    if left <= start and end <= right :
        return tree[node]
    
    mid = int((start + end) / 2)

    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

def solution() :
    global N, Q, arr, tree, querys

    input_val()

    build(1, 1, N)
    # print(f"tree : {tree}")

    result = []

    for i in querys :
        result.append(str(query(1, 1, N, min(i[0], i[1]), max(i[0], i[1]))))
        update(1, 1, N, i[2], i[3])    

    # print(f"result : {result}")
    print("\n".join(result).strip())

if __name__ == "__main__" :
    solution()