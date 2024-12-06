from math import pow

N, K = map(int, input().split())
students = list([int(input()) for _ in range(N)])
fulluse = int(pow(2, N)) - 1
final_count = 0
dp = [[0 for _ in range(fulluse + 1)] for _ in range(N)]

def solve(start_stu, bit) : # start_stu는 학생의 index, N은 배열을 시작 하는 수, bit는 현재 사용하지 않은 수, return은 start로 시작 하는 모든 수
    if dp[start_stu][bit] : return dp[start_stu][bit]
    if (bit == fulluse) : 
       dp[start_stu][bit] = 1
       return 1
    
    tmp_bit = (bit | int(pow(2, start_stu)))
    count = 0 
    for i in range(N) :
        if (tmp_bit & int(pow(2, i)) == 0) and abs(students[start_stu] - students[i]) > K :
            count += solve(i, tmp_bit | int(pow(2, i)))
    dp[start_stu][bit] = count
    return count
    
for i in range(N) : 
    final_count += solve(i, int(pow(2, i)))

print(final_count)