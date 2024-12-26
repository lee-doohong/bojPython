import sys
import copy

rl = sys.stdin.readline
arr_list = []

def make_reverse(arr) :
    tmp_arr = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N) :
        for y in range(N) :
            tmp_arr[x][y] = arr[y][x]

    return tmp_arr
 
def multiply(arr1, arr2) :
    for i in range(len(arr1)) :
        if (arr1[i] * arr2[i]) == 1 : 
            return 1
    return 0

def matrix_multiply(arr1_2d, arr2_2d) :
    arr2_2d_r = make_reverse(arr2_2d)
    empty_arr = [[0 for _ in range(N)] for _ in range(N)]
    
    for x in range(N) : # 실제 행렬 곱하기
            for y in range(N) :
                empty_arr[x][y] = multiply(arr1_2d[x], arr2_2d_r[y])
    
    return empty_arr

def matrix_multiply_r(arr1_2d, arr2_2d_r) :
    empty_arr = [[0 for _ in range(N)] for _ in range(N)]
    
    for x in range(N) : # 실제 행렬 곱하기
            for y in range(N) :
                empty_arr[x][y] = multiply(arr1_2d[x], arr2_2d_r[y])
    
    return empty_arr

def make_list(arr_target) :
    tmp_arr = [a[:] for a in arr_target]
    arr_list.append(tmp_arr)
    for _ in range(20) :
        tmp_arr = matrix_multiply(tmp_arr, tmp_arr)
        arr_list.append(tmp_arr)

if __name__ == "__main__" :
    input_line = list(map(int, rl().split()))
    N = input_line[0]; K = input_line[1]; M = input_line[2]

    result = []

    arr = [[0 for _ in range(N)] for _ in range(N)] # 기본행렬

    for i in range(N) :
        tmp_arr = rl().split()
        arr[i][int(tmp_arr[0]) - 1] = 1
        arr[i][int(tmp_arr[1]) - 1] = 1

    make_list(arr)

    K_list = list(bin(K)[2:])
    K_list.reverse()

    result_arr = [[0 for _ in range(N)] for _ in range(N)]
    flag = True

    for i in range(len(K_list)) :
        if K_list[i] == "1" :
            if flag :
                result_arr = arr_list[i]
                flag = False
            else : result_arr = matrix_multiply(result_arr, arr_list[i])

    for i in range(M) :
        tmp_arr = rl().split()
        if result_arr[int(tmp_arr[0]) - 1][int(tmp_arr[1]) - 1] == 1 :
            result.append("death")
        else :
            result.append("life")

    "\n".join(result)        
    print("\n".join(result))