import sys
import math

N = int(input())
cities = []
for i in range(N) :
    cities.append(list(map(int, sys.stdin.readline().split()))) 

map = [[0 for _ in range(N)] for _ in range(N)]

visited_all = (1<<N) - 1

INF = float('inf')
dp = [[INF for _ in range(N)] for _ in range(visited_all + 1)]
result = INF

def get_distance(x, y) :
    return math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2))

def make_map() :
    global map
    
    for i in range(N) :
        for j in range(N) :
            if (map[i][j] != 0) : continue
            elif i == j : continue
            else :
                dis_tmp = get_distance(cities[i], cities[j])
                map[i][j] = dis_tmp; map[j][i] = dis_tmp

def dfs(visited, now_pos, now_value) :
    global result
    if(visited == visited_all) :
        result = min(now_value + map[now_pos][0], result)
        return

    for i in range(N) :
        if visited & (1<<i) == 0 and now_value + map[now_pos][i] < dp[visited | (1<<i)][i] : # 방문하지 않은 장소인 경우에만
            dp[visited | (1<<i)][i] = now_value + map[now_pos][i]
            dfs(visited | (1<<i), i, dp[visited | (1<<i)][i])

if __name__ == "__main__" :
    make_map()
    dfs(1, 0, 0) # 1번 도시만 방문했고, 현재 위치는 0이다, 현재까지 소비된 거리값도 0이다.
    print(result)