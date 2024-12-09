#T의 갯수를 최대한 줄이기
#T를 0으로, H를 1으로..
import sys

rl = sys.stdin.readline
N = int(input())
xor_N = (1 << N) - 1

arr = [int(rl().strip().replace('H', '1').replace('T', '0'), 2) for _ in range(0, N)]
arr_asmbl = []

def dfs(n, prcs_arr) :
    global arr_asmbl
    print(f'f : {n}, prcs_arr : {prcs_arr}')
    if n == N :
        arr_asmbl.append(prcs_arr)
        return
    
    dfs(n+1, prcs_arr)
    prcs_arr[n] = prcs_arr[n] ^ xor_N
    dfs(n+1, prcs_arr)

def to_bin_arr(a) :
    # tmp_arr = []
    for i in range(len(arr)) :
        a.append('{0:0>3}'.format(bin(a[i])[2:]))
    return a

if __name__ == '__main__' :
    print(f'arr(bin) : {to_bin_arr(arr)}')
    print(f'arr : {arr}')
    dfs(0, arr)
    print(f'arr(after) : {arr}')
    for i in arr_asmbl : 
        print(i)


