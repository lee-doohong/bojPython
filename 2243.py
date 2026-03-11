from sys import stdin

N = int(stdin.readline())
tree = [0] * (10**6) * 4
result = []

def input_val() :
    return list(map(int, stdin.readline().strip().split()))

def update(node, start, end, index, val) :
    # print(f"[update] node {node} start {start} end {end} index {index} val {val}")
    if index < start or end < index : 
        return
    
    if start == end == index : 
        tree[node] += val
        # print(f"tree[{node} , start {start}] = {tree[node]}")
        return
    
    mid = int((start + end) / 2) 
    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

# 이게 핵심 몇번째 사탕을 라고 햇을때 그 사탕의 당도를 뱉고 해당 노드 -1 업데이트 해주는게 핵심임
def query(node, start, end, index) :
    # print(f"[query] node {node} start {start} end {end} index {index}")
    # 리프노드까지 도착한 경우 start == end인 경우 리프노드까지 도달한 것임, 당도를 뱉고 숫자 업데이트하는 것임
    if start == end :
        # 여기서 index는 진짜 인덱스가 아니라 몇번째 인가인데
        update(1, 1, 10**6, start, -1)
        result.append(str(start))
        return
    
    mid = int((start + end) / 2)
    # 리프노드까지 도착하지 않은 경우
    if tree[node * 2] >= index :
        query(node * 2, start, mid, index)
    else : 
        query(node * 2 + 1, mid + 1, end, index - tree[node * 2])

def solution() :
    for _ in range(N) :
        val_tmp = input_val()
        if val_tmp[0] == 1 :
            query(1, 1, 10**6, val_tmp[1])
        else :
            update(1, 1, 10**6, val_tmp[1], val_tmp[2])

    print("\n".join(result))

if __name__ == "__main__" :
    solution()