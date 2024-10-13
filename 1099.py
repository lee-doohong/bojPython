from sys import maxsize
from sys import stdin

rl = stdin.readline

def check(i, j) :
    target = list(rawstr[i:j+1])
    minN = maxsize
    for w in words :
        tmpN = 0
        if sorted(w) == sorted(target) : #둘이 정렬해서 같을때 w 와 target단어가 얼마나 다른지 확인해 주면 된다.
            for i in range(len(w)) :
                if w[i] != target[i] : tmpN += 1 
            minN = min(tmpN, minN)
    return minN

def DFS(i, j) :
    if (DP[i][j] != maxsize or flag[i][j] == True) : return DP[i][j]

    if (i==j) : DP[i][j] = min(check(i, j ), DP[i][j])

    for k in range(i, j) :
        DP[i][j] = min(DFS(i, k) + DFS(k+1, j), check(i, j), DP[i][j])

    flag[i][j] = True
    return DP[i][j]

rawstr = rl().strip()
strlength = len(rawstr)
N = int(rl())
words = [rl().strip() for _ in range(N)]

DP = [[int(i<=j) * maxsize for j in range(strlength)] for i in range(strlength)]
flag = [[False for j in range(strlength)] for i in range(strlength)]

result = DFS(0, len(rawstr) - 1)

print(result if result != maxsize else -1) 