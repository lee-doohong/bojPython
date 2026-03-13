from sys import stdin

N = None
a_arr = []
b_arr = []
pos = [0] * 1_000_001
tree = []

def read_line() :
    return list(map(int, stdin.readline().strip().split()))

def input_val() :
    global N, a_arr, pos, tree

    N = int(int(stdin.readline().strip()))
    a_arr = read_line()
    b_arr = read_line()
    
    for i in range(len(b_arr)) :
        pos[b_arr[i]] = i + 1 # i + 1은 위치 - 제일 첫번째 위치는 1이다. read

    tree = [0] * 4 * N

# 답 회신
def query(node, start, end, left, right) :
    # print(f"[query]node {node} start {start} end {end} left {left} right {right}")
    if right < start or end < left :
        return 0
    
    if left <= start and end <= right :
        return tree[node]

    mid = int((start + end) / 2)

    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

def update(node, start, end, index, val) :
    # print(f"[update]node {node} start {start} end {end} index {index} val {val}")
    global tree

    if index < start or end < index :
        return
    
    if start == end == index :
        tree[node] = val
        return

    mid = int((start + end) / 2)

    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def solution() :
    result = 0

    input_val()

    for i in a_arr :
        result += query(1, 1, N, pos[i], N) # 어짜피 기계의 위치는 모두 unique하니까.
        # print(f"tree {tree} result {result}")
        update(1, 1, N, pos[i], 1)

    print(result)
    return

if __name__ == "__main__" :
    solution()