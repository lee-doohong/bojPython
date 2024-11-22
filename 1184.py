import sys

read = sys.stdin.readline

N = int(input())
field = [list(map(int, read().split())) for _ in range(N)]
cnt = 0

def solve(x, y) :
    global cnt
    list1,list2,list3,list4 = []

    list2 = get_extent(x, y, 2)
    list3 = get_extent(x, y, 3)

    if (x - 1 >= 0 and y + 1 <= N - 1) :
        list1 = get_extent(x - 1, y + 1, 1)

    if (x + 1 <= N - 1 and y + 1 <= N - 1) :
        list4 = get_extent(x + 1, y + 1, 4)

    if (list1) :
        for i in list1 :    
            for j in list3 :
                cnt += 1 if i==j else 0
    if (list4) :
        for i in list2 :    
            for j in list4 : 
                cnt += 1 if i==j else 0

def get_extent(x, y, q) :
    tmp_list = []
    tmp_field = [[0 for _ in range(N)] for _ in range(N)]
    
    match q :
        case 1:
            for i in reversed(range(0, x + 1)) :
                tmp = 0
                for j in range(y, N) :
                    tmp += field[i][j]#해당 줄의 값
                    try : 
                        tmp_field[i][j] = tmp + tmp_field[i + 1][j]
                    except : #줄밖으로 나가는 경우
                        tmp_field[i][j] = tmp    
                    tmp_list.append(tmp_field[i][j])
            return tmp_list    
        case 2:
            for i in reversed(range(x + 1)) :
                tmp = 0
                for j in reversed(range(y + 1)) :
                    tmp += field[i][j]#해당 줄의 값
                    try : 
                        tmp_field[i][j] = tmp + tmp_field[i + 1][j]
                    except : #줄밖으로 나가는 경우
                        tmp_field[i][j] = tmp    
                    tmp_list.append(tmp_field[i][j])
            return tmp_list
        case 3:
            for i in range(x, N) :
                tmp = 0
                for j in reversed(range(y+1)) :
                    tmp += field[i][j]#해당 줄의 값
                    try : 
                        tmp_field[i][j] = tmp + tmp_field[i - 1][j]
                    except : #줄밖으로 나가는 경우
                        tmp_field[i][j] = tmp    
                    tmp_list.append(tmp_field[i][j])    
            return tmp_list
        case 4:
            for i in range(x, N) :
                tmp = 0
                for j in range(y, N) :
                    # print(f'x : {i}, y : {j}')
                    tmp += field[i][j]#해당 줄의 값
                    try : 
                        tmp_field[i][j] = tmp + tmp_field[i - 1][j]
                    except : #줄밖으로 나가는 경우
                        tmp_field[i][j] = tmp    
                    tmp_list.append(tmp_field[i][j])   
            return tmp_list

if __name__ == '__main__' :
    for i in range(N) :
        for j in range(N) :
            solve(i, j)

    print(cnt)