import sys
import math

N =  int(input())

arr = list(map(int, [input() for _ in range(N)]))
arr.sort()
# print(arr)
#방문한 경우에는 True로 바꿔준다.
visited = [[False for _ in range(N)] for _ in range(N)]

final_cnt = 1

# visited[i][j] : i에서 j로 가는걸 확인했다는 의미이다. - 여기서 i와 j는 첫번째와 그 다음 수가 
#아니고 그냥 등차가 성립하는 모든 수
# 시간 복잡도가 n^3인데 visited 통해서 최대한 줄이는게 핵심
# 3중 for 문을 돌릴껀데 일단 등차의 첫번째 시작하는 수가 첫번째 for문이고
# 두번째 수부터 확인하는데 등차가 몇인지 확인하고 그 이후로는 그거랑 등차가 맞는 수가 있는지
# 지속적으로 확인 하고 최대 길이 확인하는 방식으로 하면 되겠네..

def solution() :
    global visited
    global final_cnt
    
    for i in range(N) :
        # 첫번째 수는 first_N
        first_index = i
        second_index = 2001
        cnt_tmp = 1

        # print("for_1st, fist_index : {0}, second_index : {1}, cnt_tmp : {2}".format(first_index, second_index, cnt_tmp))

        for j in range(i + 1, N) :
            #방문한 적이 있다면 패스
            if(visited[i][j] == True) :
                continue
            else : visited[i][j] = True

            #등차의 기준이 되는 수 지정
            second_index = j
            #공차확인
            common_dif = arr[second_index] - arr[first_index]
            #카운트 하나 더 올려준다
            cnt_tmp = 2

            # print("for_2st, fist_index : {0}, second_index : {1}, cnt_tmp : {2}, common_dif : {3}".format(first_index, second_index, cnt_tmp, common_dif))
            
            for k in range(j + 1, N) :
                # 바로 직전 숫자와 등차가 같다면..  
                if ((arr[k] - arr[second_index]) > common_dif) :
                    break

                if ((arr[k] - arr[second_index]) == common_dif) :
                    if(visited[second_index][k] == True) :
                        # 같은 차이가 나는 수를 확인했는데 이미 방문한 적이 있다면 굳이 더 할필요가 없으므로 break 한다.
                        break
                    else : visited[second_index][k] = True

                    cnt_tmp += 1
                    second_index = k

                # print("for_3st, fist_index : {0}, second_index : {1}, k : {4} cnt_tmp : {2}, common_dif : {3}".format(first_index, second_index, cnt_tmp, common_dif, k))

            final_cnt = max(final_cnt, cnt_tmp)
    return

if __name__ == "__main__" : 
    solution()
    # print("final_cnt : {0}".format(final_cnt))
    print(final_cnt)



