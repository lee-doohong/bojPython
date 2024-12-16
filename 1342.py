import math

N = int(input())

arr_list = []

class node :
    def __init__(self, n) :
        self.n = n
        self.min = int((n*(n + 1)) / 2)
        self.max = int(math.pow(2, n)) - 1

    def __str__(self) : 
        return f'n : {self.n} min : {self.min}, max : {self.max}'

if __name__ == "__main__" :
    print("__main__")
    for i in range(20) :
        arr_list.append(node(i))

    for i in arr_list :
        tmp_arr = []
        if (N >= min & N <= max) :
            tmp_arr.append(i)

        if not tmp_arr :
            print(-1)
        
        tmp_arr[0] # 이게 이제 대상 수인데... 가장 빠른 수 문자열 어케 찾지?
        

