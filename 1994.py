N =  int(input())

arr = list(map(int, [input() for _ in range(N)]))
arr.sort()

#방문한 경우에는 True로 바꿔준다.
visited = [[False for _ in range(N)] for _ in range(N)]

# visited[i][j] : i에서 j로 가는걸 확인했다는 의미이다. - 여기서 i와 j는 첫번째와 그 다음 수가 
#아니고 그냥 등차가 성립하는 모든 수
# 시간 복잡도가 n^3인데 visited 통해서 최대한 줄이는게 핵심
# 3중 for 문을 돌릴껀데 일단 등차의 첫번째 시작하는 수가 첫번째 for문이고
# 두번째 수부터 확인하는데 등차가 몇인지 확인하고 그 이후로는 그거랑 등차가 맞는 수가 있는지
# 지속적으로 확인 하고 최대 길이 확인하는 방식으로 하면 되겠네..

def solution() :
    global visited
    
    for i in range(N) : 
        first_N = arr[i]
        now_N
        for j in range(i + 1, N) :

            if(visited[i][j] == True) :
                continue
            else : visited[i][j] = True

            common_dif = arr[j] - first_N
            
            if (arr[j])

    
    return

if __name__ == "__main__" : 
    solution() 



