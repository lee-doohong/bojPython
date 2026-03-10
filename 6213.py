from sys import stdin, maxsize

N = Q = None
arr = []
tree = []


def read_val() :
    return list(map(int, stdin.readline().strip().split()))

def input_val() :
    global N, Q, arr, tree

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

    tree[node] = [min(result1[0], result2[0]), max(result1[1], result2[1])]
    return(tree[node])

def query(node, start, end, left, right) :
    if right < start or end < left :
        return [maxsize, -1 * maxsize]
    
    if (left <= start and end <= right) :
        return tree[node]

    mid = int((start + end) / 2)

    result1 = query(node * 2, start, mid, left, right)
    result2 = query(node * 2 + 1, mid + 1, end, left, right)

    return [min(result1[0], result2[0]), max(result1[1], result2[1])]

def solution() :
    input_val()

    build(1, 1, N)

    result = []

    for _ in range(Q) :
        Q_line = read_val()
        result_tmp = query(1, 1, N, Q_line[0], Q_line[1])
        result.append(str(result_tmp[1] - result_tmp[0]))
        result_tmp = []

    print("\n".join(result))

if __name__ == "__main__" :
    solution()