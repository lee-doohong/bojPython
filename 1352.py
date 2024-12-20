import math

N = int(input())
limit = 0
arr_list = []
result = []

class node :
    def __init__(self, n) :
        self.n = n
        self.min = int((n*(n + 1)) / 2)
        self.max = int(math.pow(2, n)) - 1

    def __str__(self) : 
        return f'n : {self.n} min : {self.min}, max : {self.max}'

# 가장 빠르다는 뜻이 무엇일까... ABCCCC 보다 ABBCCC가 더 빠르다고 볼 수 있다. 즉, 가장 멀리 갈수록 빠르다고 볼 수 있음
# ABBCC 1248 과 1236과 1245의 길이는 같을거다 둘다 12임.. 하지만 여기서 뭐가 더 빠를까 1245가 더 빠르다....
# 그럼 멀리갈 수록 더 빠르니까 문자가 최대 길이로 가는것 부터 검토해주면 된다.
def DFS(n, arr_deliver) : #
    global result
    # print(f'[DFS] n : {n}, arr_deliver : {arr_deliver}')
    if len(arr_deliver) >= limit : # 범위 벗어나는 경우 종료
        # print(f'arr_deliver 길이 초과! 길이 : {arr_deliver}')
        return

    for i in range(sum(arr_deliver) + 1, n - 1, -1) : #n부터 arr에 들어있는 합 + 1 까지 위치를 검토해준다.(선택 가능한 범위니까)
        # print(f'[in for] arr_deliver : {arr_deliver}, i : {i}')
        tmp_length = i + sum(arr_deliver) #임시길이
        if (tmp_length == N) :
            # print(f'[tmp_length == N] tmp_length = {tmp_length})')
            result = arr_deliver + [i]
        if(tmp_length < N) :
            DFS(i + 1, arr_deliver + [i])

def make_string(arr) : 
    result_string = ""
    num = 1

    # for i in arr : # 일단 빈칸 채우기
    #     result_string[i] = i

    for i in arr :
        flag = True
        for j in range(i) :
            if len(result_string) >= i and flag:
                # print(f'len(result_string) : {result_string}, i : {i}, flag : {flag}')
                result_string = result_string[0:i - 1] + str(num) + result_string[i-1:]
                flag = False
                continue
            result_string = result_string + str(num)
        num += 1

    for i in range(num) :
        result_string = result_string.replace(chr(i + 48), chr(i + 64))

    # print(f'[make_string] result_strig : {result_string}')
    print(result_string)
        


if __name__ == "__main__" :
    for i in range(20) :
        arr_list.append(node(i))

    tmp_arr = []
    
    for i in arr_list :
        if (N >= i.min and N <= i.max) :
            tmp_arr.append(i)

    if not tmp_arr :
        print(-1)
    else : 
        limit = tmp_arr[0].n
        DFS(1, [])
        # print (f'result : {result}')

        make_string(result)

    
        

