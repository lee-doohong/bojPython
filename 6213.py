from sys import stdin, maxsize

N = Q = None
arr = []
tree = []

def read_val() :
    return list(map(int, stdin.readline().strip().split()))

def input_val() :
    global N, Q, arr

    N, Q = read_val()

    arr = [0]

    for _ in range(N) : 
        arr.append(int(input()))

    tree = [0] * 4 * N

def build(node, start, end) :
    if start == end : 
        tree[node] = [arr[start], arr[start]]
        return tree[node]
    
    mid = int((start + end) / 2)

    result1 = build(node * 2, start, mid)
    result2 = build(node * 2 + 1, mid + 1, end)
    result1.extend(result2)

    tree[node] = [min(result1), max(result1)]
    
    return(tree[node])

# 뺀 값을 반환하면 안되고 [최소, 최대] 리스트를 반환해야 한다.
def query(node, start, end, left, right) :
    if start == end :
        return tree[node]
    
    if right < start or end < left :
        return [maxsize, -1 * maxsize] 

    mid = int((start + end) / 2)

    result1 = query(node * 2, start, mid)
    result2 = query(node * 2 + 1, mid + 1, end)
    result1.extend(result2)

    return [min(result1), max(result1)]

def solution() :
    input_val()

    build(1, 1, N)

    result = []

    for _ in range(Q) :
        Q_line = read_val()
        result_tmp = query(1, 1, N, Q_line[0], Q_line[1])
        result.append(str(result_tmp[1] - result_tmp[0]))

    print("\n".join(result))

if __name__ == "__main__" :
    solution()