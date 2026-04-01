from sys import stdin
import collections

def solution() :
    N = int(stdin.readline())
    M = int(stdin.readline())

    Q = collections.deque()

    indegree = [0] * (N + 1)
    adj = [[] for _ in range(N + 1)]
    count = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M) :
        X, Y, K = list(map(int, stdin.readline().split()))
        indegree[X] += 1
        adj[Y].append([X, K])
    
    basic = [] 
    
    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            Q.append(i)
            basic.append(i)
            count[i][i] = 1

    while Q :
        now = Q.popleft()
        for i, j in adj[now] :
            for b in basic :
                count[i][b] += count[now][b] * j

            indegree[i] -= 1
            if not indegree[i] : Q.append(i)

    result = []
    for b in basic :
        result.append(f"{b} {count[N][b]}")
    
    print("\n".join(result))
    return

if __name__ == "__main__" :
    solution()