#T의 갯수를 최대한 줄이기
#T를 0으로, H를 1으로..
import sys
import copy
from itertools import combinations

rl = sys.stdin.readline
N = int(input())

xor_N = (1 << N) - 1

arr_raw = [int(rl().strip().replace('H', '1').replace('T', '0'), 2) for _ in range(0, N)]
arr_raw_rev = [i ^ xor_N for i in arr_raw]

arr_num = [i for i in range(N)]
arr_asmbl = []

min_N = sys.maxsize

def dfs(n, processing_arr) :
    global min_N
    if n == N :
        min_N = min(row_cal(processing_arr), min_N)
        return
    
    # print(f'f : {n}, prcs_arr : {processing_arr}')
    dfs(n+1, processing_arr)
    
    tmp_arr = copy.deepcopy(processing_arr)
    tmp_arr[n] = processing_arr[n] ^ xor_N
    dfs(n+1, tmp_arr)

def make_comb(n) :
    # global arr_asmbl
    global min_N
    for i in combinations(arr_num, n) :
        tmp_arr = []
        for j in range(N) :
            if j in i :
                tmp_arr.append(arr_raw[j])
            else : 
                tmp_arr.append(arr_raw_rev[j])
        min_N = min(row_cal(tmp_arr), min_N)
        # arr_asmbl.append(tmp_arr)

def make_comb2() :
    global arr_asmbl
    global min_N
    for bit in range(1<<N) : #모든 경우의 수에 대해서
        tmp_arr = []
        for i in range(N) :
            if(bit & 1 << i) :
                tmp_arr.append(arr_raw[i] ^ xor_N)
            else : tmp_arr.append(arr_raw[i])

        min_N=min(row_cal(tmp_arr), min_N) 

            
def to_bin_arr(arr) :
    tmp_arr = ""
    for i in range(len(arr)) :
        tmp_arr += "{0:0>3}".format(bin(arr[i])[2:]) + "\n"
    return tmp_arr

def row_cal(arr) :
    # print(f'[row_cal] arr : {arr}')
    global min_N

    return_N = 0

    for i in range(len(arr)) :
        tmp_N = 1 << i
        T_num_tmp = 0
        H_num_tmp = 0    
        for l in arr :
            # print(f'tmpN : {tmp_N}')
            # print(f'l[i] : {l}')
            if(tmp_N & l) : H_num_tmp += 1
            else : T_num_tmp += 1
        return_N += min(T_num_tmp, H_num_tmp)
    # print(f'[row_cal] return_N : {return_N}')
    return return_N

if __name__ == '__main__' :
    # print(f'arr(bin) : {to_bin_arr(arr_raw)}')
    # print(f'arr : {arr_raw}')
    # dfs(0, arr_raw)
    # print(f'arr(after) : {arr_raw}')
    

    # print(min_N)

    # print(to_bin_arr(arr_raw))
    # print(to_bin_arr(arr_raw_rev))
    # print(arr_num)
    for i in range(N + 1) : 
        make_comb(i)
    # print(arr_asmbl)

    # make_comb2()

    # for i in arr_asmbl : 
    #     min_N = min(min_N, row_cal(i))
    print(min_N)



