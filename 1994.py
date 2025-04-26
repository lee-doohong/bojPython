import sys
import math
from collections import Counter

N =  int(input())

arr_tmp = list(map(int, [input() for _ in range(N)]))

num_counter = Counter(arr_tmp)
final_cnt = num_counter.most_common(1)[0][1]

arr = list(set(arr_tmp))
arr.sort()
N = len(arr)

visited = [[False for _ in range(N)] for _ in range(N)]

def binary_search(start, end, target_N) :
    while(start <= end) : #start가 end보다 큰 동안 진행한다.
        mid = int((start + end) / 2)
        if (arr[mid] == target_N) :
            return mid
        elif (arr[mid] < target_N) : #가운데 있는 수가 타겟 숫자보다 작다 > start가 mid가 된다.
            start = mid + 1
        else : end = mid - 1
    return -1        

def solution() :
    global visited
    global final_cnt
    
    for i in range(N) :
        first_index = i
        second_index = 2001
        cnt_tmp = 1

        for j in range(i + 1, N) :
            if(visited[i][j] == True) :
                continue
            else : visited[i][j] = True

            second_index = j
            common_dif = arr[second_index] - arr[first_index]
            cnt_tmp = 2

            start = j
            while(1) :
                tmp_J = binary_search(start, N - 1, arr[start] + common_dif)
                if (tmp_J == -1 or visited[start][tmp_J]) : break
                else :
                    visited[start][tmp_J] = True
                    start = tmp_J 
                    cnt_tmp += 1
                    
            final_cnt = max(final_cnt, cnt_tmp)
    return

if __name__ == "__main__" : 
    solution()
    print(final_cnt)