from sys import maxsize
from sys import stdin

def rl() :
    return stdin.readline()

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
    # print("[DFS] i : {0} j : {1}".format(i, j))
    if (DP[i][j] != maxsize or flag[i][j] == True) : return DP[i][j]

    for k in range(i, j) :
        DP[i][j] = min(DFS(i, k) + DFS(k+1, j), check(i, j), DP[i][j])

    flag[i][j] = True
    return DP[i][j]

rawstr = rl().strip()
strlength = len(rawstr)
N = int(rl())
words = []
for _ in range(N) :
    words.append(list(rl().strip()))

# DP초기화
DP = [[int(i<=j) * maxsize for j in range(strlength)] for i in range(strlength)]
flag = [[False for j in range(strlength)] for i in range(strlength)]

result = DFS(0, len(rawstr) - 1)


print(result if result != maxsize else -1)


# 다이나믹 프로그래밍을 사용 하면 될거 같은데
# 서로 정렬을 한 다음 같으면 그때 부터는 갯수를 세어본다.
# 단어를 쪼개서 각 문장에 일치하는 단어가 있는지 확인해본다.
#파이썬에서는 list == list로 순서 등을 비교할 수 있다.
# 특정 문자열 어디부터 어디까지 잘라서 뭐랑 비교하나?
# 어째튼 가장 작은 값을 찾아야 하니..
# 예를 들어 
# abcde 라는 문장이 있고
# a bcd e 
# 생각 못한 부분이 뭘까..?
# 해석이 안된 부분이 있다면?
# 여기서 만약 a 가 해석이 안되었다
# 하지만 bcd는 해석이 되었다 치자..
# 그런데 세개 네개로 나뉘는 경우가 있을 수 있을 것이다.
# 즉 a bcd 로 나뉘었다고 한다면 그럼 이미 a bcd에서 최솟 값으로 되어 있을 것이다.
# dp는 탑다운 방식으로 할까.. 전체-> 소수...가는 방식으로
# 그냥 for 문으로 돌리면 문제가 생김
# 특정 문장에 대해  최소값 찾는 함수 만들고 전체에 대해 시행한 다음 그 전체가 부분부분을 찾는 방식으로..
# 어디..
# 그래서 결국 문제가 없을수 있고 check는 전체에 대해서만 하면 된다.
# dp는 이미 계산이 다 된 것을 전제로 해야 하는데
# abc / de / abced 라는 단어가 있다고 치자
# 그럼 dp[0][2] + dp[3][4] 가 최소 값이 될 것이다.
# 저 문장에서 해석이 안되는 부분은 없어야 할 것이다.
# 해석할 수 있는 최소값이라는게 뭐지?
#dnjf 문장 전체는 해석이 되어야만 한다...?
# 즉 해석이 안되는 부분이 있어서는 안된다는 의미인데..
# 그럼 점화식을 어떻게 만드는 것이 좋을까
# de 라는 단어가 있다고 치자 그럼 최저 값을 찾으면 될 것이다.
# dp는 최대값으로 