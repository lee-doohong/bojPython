from sys import stdin

def input_bj() :
    return list(map(int, stdin.readline().split()))

def solution() :
    N, K = input_bj()
    burdens = []

    for _ in range(N) :
        burdens.append(input_bj())

    # print(burdens)

    dp = [[0]* (K + 1) for _ in range(N)]

    for i in range(N) :
        weight, value = burdens[i]

        if not i :
            for w in range(weight, K + 1) :
                dp[i][w] = value
            continue    
            
        for w in range(K + 1) :
            if (w - weight) < 0 :
                dp[i][w] = dp[i - 1][w]
            else : 
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])

    # print(dp)
    print(dp[N - 1][K])

if __name__ == "__main__" : 
    solution()