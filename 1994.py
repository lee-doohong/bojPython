# import sys
# import math
# from collections import Counter

# N =  int(input())

# arr_tmp = list(map(int, [input() for _ in range(N)]))

# num_counter = Counter(arr_tmp)
# final_cnt = num_counter.most_common(1)[0][1]

# arr = list(set(arr_tmp))
# arr.sort()
# N = len(arr)

# visited = [[False for _ in range(N)] for _ in range(N)]

# def binary_search(start, end, target_N) :
#     while(start <= end) : #start가 end보다 큰 동안 진행한다.
#         mid = int((start + end) / 2)
#         if (arr[mid] == target_N) :
#             return mid
#         elif (arr[mid] < target_N) : #가운데 있는 수가 타겟 숫자보다 작다 > start가 mid가 된다.
#             start = mid + 1
#         else : end = mid - 1
#     return -1        

# def solution() :
#     global visited
#     global final_cnt
    
#     for i in range(N) :
#         first_index = i
#         second_index = 2001
#         cnt_tmp = 1

#         for j in range(i + 1, N) :
#             if(visited[i][j] == True) :
#                 continue
#             else : visited[i][j] = True

#             second_index = j
#             common_dif = arr[second_index] - arr[first_index]
#             cnt_tmp = 2

#             start = j
#             while(1) :
#                 tmp_J = binary_search(start, N - 1, arr[start] + common_dif)
#                 if (tmp_J == -1 or visited[start][tmp_J]) : break
#                 else :
#                     visited[start][tmp_J] = True
#                     start = tmp_J 
#                     cnt_tmp += 1
                    
#             final_cnt = max(final_cnt, cnt_tmp)
#     return

# if __name__ == "__main__" : 
#     solution()
#     print(final_cnt)

from collections import defaultdict

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

if N <= 2:
    print(N)
else:
    nums.sort()
    dp = [defaultdict(int) for _ in range(N)]
    max_len = 1

    for i in range(N):
        for j in range(i):
            diff = nums[i] - nums[j]
            # The length of the arithmetic progression ending at nums[i] with the
            # common difference 'diff' is the length of the AP ending at nums[j]
            # with the same difference, plus 1 (for nums[i] itself).
            # If there's no such AP ending at nums[j], it means the current
       +     # AP starts with nums[j] and nums[i], so its length is 2.
            dp[i][diff] = dp[j][diff] + 1 if dp[j][diff] else 2
            max_len = max(max_len, dp[i][diff])

    print(max_len)*+*+**++*+*+*+*+*+*+*+*+*+**+