import sys
#함수정의
rl = sys.stdin.readline

N, M = list(map(int, rl().strip().split()))
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
totalliter = 0

def BFS(i, j) :
    queue = []; queue.append([i, j])
    floorPool[i][j] = False
    liter = 0
    flag = True
    while queue : #queue가 비어있지 않은 동안
        i, j = queue.pop() #queue에서 하나 뽑는다
        liter += 1
        for d in direction :
            nI = i + d[0]; nJ = j + d[1]
            if nI < 0 or N - 1 < nI or nJ < 0 or nJ > M - 1 : # 범위 밖으로 나가버리는 경우
                flag = False
            else :
                if floorPool[nI][nJ] == True : # 수영장 바닥이 낮아지면
                    queue.append([nI, nJ])
                    floorPool[nI][nJ] = False
    return liter if flag else 0 

def search(floor) :
    liter = 0

    global floorPool; floorPool = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N) : #해당 층을 탐색한다.
        for j in range(M) :
            floorPool[i][j] = True if pool[i][j] < floor else False

    for i in range(N) : # 해당 층의 수영장에서 True인 부분은 BFS 태운다
        for j in range(M) :
            if floorPool[i][j] is True : 
                liter += BFS(i, j)

    return liter

pool = [list(map(int, [*input().strip()])) for _ in range(N)]

height = 0

for i in pool : 
    for j in i :
        height = max(height, j)

for i in range (2, height + 1) :
    totalliter += search(i)

print(totalliter)
