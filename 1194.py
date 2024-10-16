import sys

rl = sys.stdin.readline
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
key = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5}


def BFS(key, i, j) :
    q = []; q.append([i, j])

    while q :
        tmp = q.pop()
        for d in direction : 
            ni = tmp[0] + d[0]; nj = tmp[1] + d[1]
///            if (map[ni, nj] == '')
    return

N, M = map(int, rl().split())

# map 생성
map = [[*input()] for _ in range(0, M)]

start = [] 

# i에서 시작한다
for i in range(N) : 
    for j in range(M) :
        if map[i][j] == '0' :   
            start = [i, j]

DP = [N][M][64]


BFS(start[0], start[1])