from sys import stdin
import sys

N = None
runners = []
tree = []

def input_val() :
    global N, runners, tree

    N = int(stdin.readline())
    tree = [0] * N * 2
    
    runners = [int(stdin.readline()) for _ in range(N)]
    # print(f"runners : {runners}")
    sorted_runners = sorted(runners)

    runners_dictionary = {b : a for a, b in enumerate(sorted_runners)}

    for i in range(len(runners)) :
       runners[i] = runners_dictionary[runners[i]]

def update(node, start, end, index, val) :
    if index < start or end < index :
       return
   
    if start == end :
       tree[node] = val
       return
    
    mid = (start + end) // 2 

    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return 

def query(node, start, end, left, right) :
    if right < start or end < left : 
       return 0
    
    if left <= start and end <= right : 
       return tree[node]
    
    mid = (start + end) // 2 

    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)
    
def solution() :
    input_val()

    enable_overtake_num = []
    result = []

    for i in runners :
       enable_overtake_num.append(query(1, 1, N, 1, i))
       update(1, 1, N, i, 1)

    for i in range(N) :
       tmp_rank = i + 1 - enable_overtake_num[i]
       result.append(str(tmp_rank) if tmp_rank > 0 else "1")
   
    sys.stdout.write("\n".join(result))
 
if __name__ == "__main__" :
   solution()