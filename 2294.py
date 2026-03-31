from sys import stdin

n = k = None

def solution() :
    # n은 동전의 종류 입력 횟수 // k는 조합으로 만들어 내야 하는 수

    n, k = list(map(int, stdin.readline().split()))

    coins = list(set(int(stdin.readline()) for _ in range(n)))

    # dp[0] -> 0 // dp[k] -> k를 만들수 있는 최소 동전 갯수

    dp = [10001] * (k + 1) 

    dp[0] = 0

    for coin in coins :
        # dp[k] 까지 검토
        for i in range(coin, k + 1) :
           if dp[i - coin] + 1 < dp[i] :
               dp[i] = dp[i - coin] + 1

    print (dp[k] if dp[k] != 10001 else -1)

    return

if __name__ == "__main__" :
    solution()