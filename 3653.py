from sys import stdin

def input_v() : 
    return stdin.readline()

def sub_solution(n, m, movies) : # arr은 보려고 하는 영화
    tree = [0] * (n + m) * 4
    arr = [0] * m + [1] * n

    index = {i : i + m - 1 for i in range(1, n + 1)}
    tmp_result = []
     
    def build(node, start, end) : 
        if start == end :
            tree[node] = arr[start]
            return tree[node]
        
        mid = int((start + end) / 2)
        tree[node] = build(node * 2, start, mid) + build(node * 2 + 1, mid + 1, end)
        return tree[node]

    def update(node, start, end, index, val) :
        if index < start or end < index : 
            return 
        
        if start == end == index : 
            tree[node] += val
            return
        
        mid = int((start + end) / 2)
        update(node * 2, start, mid, index, val)
        update(node * 2 + 1, mid + 1, end, index, val)

        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        return
            
    def query(node, start, end, left, right) :
        if right < start or end < left :
            return 0

        if left <= start and end <= right : 
            return tree[node]
        
        mid = int((start + end) / 2)
        return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

    build(1, 0, m + n - 1)

    for i in range(m) :
        tmp_result.append(str(query(1, 0, m + n - 1, 0, index[movies[i]] - 1)))
        update(1, 0, m + n - 1, index[movies[i]], -1)
        update(1, 0, m + n - 1, m - (i + 1), 1)
        index[movies[i]] = m - (i + 1)
   
    return " ".join(tmp_result)

def solution() :
    T = int(input_v())

    result = []

    for _ in range(T) :
        n, m = list(map(int, input_v().split()))
        movies = list(map(int, input_v().split()))

        result.append(sub_solution(n, m, movies))

    print("\n".join(result))

if __name__ == "__main__" :
    solution()