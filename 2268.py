from sys import stdin

N = M = None
tree = []

def input_line() :
    return list(map(int, stdin.readline().strip().split()))

def input_val() :
    global N, M, tree

    N, M = input_line()
    tree = [0] * N * 4

def query(node, start, end, left, right) :
    if end < left or right < start :
        return 0
    
    if left <= start and end <= right :
        return tree[node]
    
    mid = int((start + end) / 2)

    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)


def update(node, start, end, index, val) :
    global tree

    # print(f"[update] node {node} start {start} end {end} index{index} val {val}")
    if index < start or end < index :
        return 
    
    if start == end == index :
        tree[node] = val
        # print(f"tree[start == end {node}] : {tree[node]}")
        return 

    mid = int((start + end) / 2)

    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    # print(f"tree[{node}] : {tree[node]}")
    return    

def solution() :
    result = []

    input_val()
    
    for _ in range(M) :
        input_val_now = input_line()

        if not input_val_now[0] : 
            result.append(str(query(1, 1, N, min(input_val_now[1], input_val_now[2]), max(input_val_now[1], input_val_now[2]))))
        else : 
            update(1, 1, N, input_val_now[1], input_val_now[2])
    
    print("\n".join(result))
    # print (f"tree : {tree}")

if __name__ == "__main__" :
    solution()
