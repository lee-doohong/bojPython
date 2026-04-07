from sys import stdin

def solution() :
    mod = 1_000_000_000
    N, K = list(map(int, stdin.readline().split()))

    # 초기화
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    
    for i in range(K + 1) :
        dp[i][0] = 1
    
    for i in range(1, K + 1) :
        for j in range(1, N + 1) :
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[K][N] % mod)

if __name__ == "__main__" :
    solution()