from sys import stdin
from collections import defaultdict

K = None
dp = None
N = M = None
lamps = defaultdict(int)

# K 끌수 있는 행인 아닌지 확인하는 합수
# K 보다 0가 적고, K - 0의 숫자가 짝수여야 함. 이 두경우 True 뱉는다.
def lamp_check(line) : 
    zero_num = 0
    for i in list(map(int, line)) :
        if not i :
            zero_num += 1
                
    return True if not ((K - zero_num) % 2) and K >= zero_num else False
    
def input_value() :
    global N, M, dp, K, lamps
    N, M = list(map(int, stdin.readline().strip().split()))
    dp = [stdin.readline().strip() for _ in range(N)]
    K = int(input())

def solution() :
    global lamps, dp

    input_value()

    # 각 줄에 대해서 lamp_check 한다음 딕셔너리에 집어 넣는 단계
    for line in dp : 
        if lamp_check(line) : # 해당 line이 끌 수 있는거면?
            lamps[line] += 1

    # max_num 체크해서 출력하는 단계
    max_num = 0
    for val in lamps.values() : 
        max_num = max(max_num, val)

    print(max_num)

if __name__ == "__main__" :
    solution()