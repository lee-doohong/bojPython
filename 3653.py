from sys import stdin

def input_v() : 
    return stdin.readline()

def sub_solution(n, m, movies) : # arr은 보려고 하는 영화
    tree = [0] * (n + m) * 4
    # n은 가지고 있는 영화의 수(1 ~ n 까지임) m은 보려고 하는 영화의 수 이다.
    # arr에서 보려고 하는 영화 때문에 비워둔건 0 ~ m - 1 까지 영화는 m 부터 m + n - 1 까지
    # 예를 들어 m이 2개 n 이 3개라면 arr에서 0 은 0부터 1까지 // 1은 2부터 4까지 
    arr = [0] * m + [1] * n
    
    # 딕셔너리로 넣자 특정 영화번호 : 위치 
    index = {i : i + m - 1 for i in range(1, n + 1)}

    tmp_result = []
     
    print(f"movies : {movies}")

    def build(node, start, end) : 
        print(f"[build] node : {node}, start : {start}, end : {end}")
        if start == end :
            tree[node] = arr[start]
            return tree[node]
        
        mid = int((start + end) / 2)
        tree[node] = build(node * 2, start, mid) + build(node * 2 + 1, mid + 1, end)

    def update(node, start, end, index, val) :
        print(f"[update] node : {node}, start : {start}, end : {end}, index : {index}, val : {val}")
        if index < start or end < index : 
            return 
        
        if start == end == index : 
            tree[node] = val
            return
        
        mid = int((start + end) / 2)
        update(node * 2, start, mid, index, val)
        update(node * 2 + 1, mid + 1, end, index, val)

        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        return
            
    def query(node, start, end, left, right) :
        print(f"[query] node : {node}, start : {start}, end : {end}, left : {left}, right : {right}")
        if right < start or end < left :
            return 0

        if left <= start and end <= right : 
            return tree[node]
        
        mid = int((start + end) / 2)
        return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

    for i in range(m) :
        tmp_result.append(str(query(1, 0, m + n - 1, 0, index[movies[i]] - 1)))
        print(f"index : {index}")
        update(1, 0, m + n - 1, index[movies[i]], -1)
        update(1, 0, m + n - 1, m - (i + 1), 1)
        index[movies[i]] = m - (i + 1)
        print(f"index : {index}")
   
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