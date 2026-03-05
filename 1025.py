from sys import stdin
from math import isqrt

N = M = None
max_perfect_square = -1
dp = None

def is_perfect_square(num) :
    return True if isqrt(num) ** 2 == num else False

def solution() :
    global dp, N, M

    N, M = list(map(int, stdin.readline().strip().split()))
    
    dp = [list(map(str, stdin.readline().strip())) for _ in range (N)]

    for i in range(N) : # 시작 위치 보내기
        for j in range(M) :
            brute_force(i, j)            

    print(max_perfect_square)

def brute_force(x, y) :
    global N, M

    for i in range(-N + 1, N) : # 위치별 등차 정해서 보내주기
            for j in range(-M + 1, M) :
                dfs(x, y, i, j, "")

def dfs(x, y, i, j, forward_value) : # 각 등차 값 다 더해서 문자열로 리턴 # i 는 가로 등차 j는 세로 등차
    # 종료 조건 i, j 가 0, 0 이거나 등차 더하기가 범위를 벗어낫거나
    global max_perfect_square
    if (i == 0 and j == 0) :
        result = int(dp[x][y])
        max_perfect_square = max(max_perfect_square, result) if is_perfect_square(result) else max_perfect_square
        return

    interim_result = int(forward_value + dp[x][y])
    max_perfect_square = max(max_perfect_square, interim_result) if is_perfect_square(interim_result) else max_perfect_square

    if(0 <= x + i < N and 0 <= y + j < M) :
        dfs(x+i, y+j, i, j, str(interim_result))
    else : return

if __name__ == "__main__" :
    solution()