import math

N = int(input())
limit = 0
result = []

class node :
    def __init__(self, n) :
        self.n = n
        self.min = int((n*(n + 1)) / 2)
        self.max = int(math.pow(2, n)) - 1

arr_list = [node(i) for i in range(20)]

def DFS(n, arr_deliver) : # 여기서 n은 다음 검토 위치?
    global result
    if len(arr_deliver) >= limit : return

    for i in range(n, sum(arr_deliver) + 2) : #n부터 arr에 들어있는 합 + 1 까지 위치를 검토해준다.(선택 가능한 범위니까)
        tmp_length = i + sum(arr_deliver) #임시길이
        if (tmp_length == N) :
            result = arr_deliver + [i]
        if(tmp_length < N) :
            DFS(i + 1, arr_deliver + [i])

def make_string(arr) : 
    result_string = ""
    num = 1

    for i in arr :
        flag = True
        for j in range(i) :
            if len(result_string) >= i and flag:
                result_string = result_string[0:i - 1] + str(num) + result_string[i-1:]
                flag = False
                continue
            result_string = result_string + str(num)
        num += 1

    for i in range(num) :
        result_string = result_string.replace(chr(i + 48), chr(i + 64))

    print(result_string)

if __name__ == "__main__" :
    tmp_arr = []
    
    for i in arr_list :
        if (N >= i.min and N <= i.max) :
            tmp_arr.append(i)

    if not tmp_arr :
        print(-1)
    else : 
        limit = tmp_arr[0].n #사용할 수 있는 문자의 갯수
        DFS(1, [])
        make_string(result)