import sys

# 2147483647 이하의 경우의 수가 나오는 경우만 한다.  
T = int(input())

dp = [0 for _ in range(100)]
dp[0] = 1; dp[1] = 1; dp[2] = 5

def dfs(n) :
    if (n < 0) : return 0
    if dp[n] != 0 : return dp[n]
    
    dp[n] = dfs(n - 1) + dfs(n - 2)*4
    for i in range(n - 3, -1, -1) :
        if ((n - i) % 2) : dp[n] += dfs(i) * 2
        else : dp[n] += dfs(i) * 3      
    return dp[n]

# 이게 왜 맞지?
    
if __name__ == "__main__" :
    # print("main")
    result = []
    
    dfs(22)

    # print(dp)

    for i in range(T) :
        result.append(str(dfs(int(input()))))

    print("\n".join(result))     