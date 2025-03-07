from sys import stdin
from math import sqrt

T = int(input())
result = []

def solution(x) :
    dis = x[1] - x[0]

    std_num = int(sqrt(dis))
    tmp_result = std_num * 2 - 1

    if (std_num ** 2 == dis) :
        result.append(str(tmp_result))
    else : 
        if dis > (std_num ** 2 + (std_num + 1) ** 2) / 2 : 
            result.append(str(tmp_result + 2))
        else :
            result.append(str(tmp_result + 1))
    # 

if __name__ == "__main__" :
    for _ in range(T) :
        solution(list(map(int, stdin.readline().split(" "))))
    
    print("\n".join(result))