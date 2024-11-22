import sys
import math
import itertools

rl = sys.stdin.readline

#input일기
N = int(rl())
fences =  sorted(rl().strip().split(), reverse=True)
maxsize = 0
#모두 다 사용한 상황
fulluse = int(math.pow(2, N) - 1)

dp = [0 for _ in range(fulluse)]

def solve(bit) :
    global maxsize
    #모든 빈칸의 3개 숫자 조합을 만들어 내야 한다.
    if dp[bit] : return dp[bit]
    print("solve")
    indexs = []#현재까지 사용하지 않은 울타리 index
    for i in range(N) :
        if (bit & int(math.pow(2, i))) == 0 :
            indexs.append(i)
    print(indexs)
    source = []    

    for a, b, c in itertools.combinations(indexs, 3) :
        print("[solve] a : {0}, b : {1}, c : {2}".format(a, b, c))
        tmpL = sorted([a, b, c], reverse = True)

        if tmpL[0] < tmpL[1] + tmpL[2] :
            tmpBit = bit | int(math.pow(2, tmpL[0])) | int(math.pow(2, tmpL[1])) | int(math.pow(2, tmpL[2])) 
            source.append(makeTri(tmpL[0], tmpL[1], tmpL[2]) + solve(tmpBit))

    #사용하지 않은 울타리 찾고 그것들의 조합을 만들어 준다.
    dp[bit] = max(source)
    return dp[bit]

def makeTri(a, b, c) :
    p = (a + b + c) / 2.0
    
    return math.sqrt(p*(p - a)*(p - b)*(p - c))



#0번째것 사용하면 math.pow(2, N)

print(fences)

print(solve(0))


