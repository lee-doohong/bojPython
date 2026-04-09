from collections import deque
from sys import stdin

def solution() :
    N = int(stdin.readline())
    # 차수를 넣을 부분
    indegree = [0] * (N + 1)
    # 각 노드(건물) 간의 관계를 넣을 부분
    graph = [[] for _ in range(N + 1)]
    # 각 건물들을 만드는데 드는 순수 시간
    time = [0] * (N + 1)
    # 각 건물들을 만드는데 드는 최소 시간(이걸 최종 줄력할 것임)
    result = [0] * (N + 1)
    
    for i in range(1, N + 1) : 
        input_str_list = list(map(int, stdin.readline().split()))
        time[i] = input_str_list[0]
        for j in input_str_list[1:] :
            if j == -1 :
                continue
            else :
                indegree[i] += 1
                graph[i].append(j)

    Q = deque()

    for i in range(1, N + 1) :
        if not indegree[i] :
            Q.append(i)

    # print(f"indegree : {indegree}")
    # print(f"graph : {graph}")
    # print(f"time : {time}")

    while Q :
        # print(Q)
        building = Q.popleft()
        max_time = 0
        
        for i in graph[building] :
            max_time = max(result[i], max_time)
        
        result[building] = time[building] + max_time
        
        for i in range(1, N + 1) :
            for j in graph[i] :
                # print(f"i : {i} j : {j}, building : {building}")
                if j == building :
                    indegree[i] -= 1
                    if not indegree[i] : 
                        Q.append(i)

    print("\n".join(list(map(str, result[1:]))))

if __name__ == "__main__" :
    solution()