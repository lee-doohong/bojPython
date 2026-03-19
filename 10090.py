from sys import stdin

def solution() :
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    tree = [0] * 2 * n
    final_result = 0

    def update(index) :
        print(f"index")
        tree[index] = 1
        while 1 :
            if not index >> 1 :
                return
            else :
                tree[index >> 1] = tree[index] + tree[index ^ 1]
                index >>= 1
    
    def query(left, right) : # left는 포함하고 right는 포함하지 않는 식으로 만들어 보자.
        tmp_result = 0
        right -= 1

        while left < right :
            if left & 1 :
                tmp_result += tree[left]
                left += 1
            if not right & 1 : 
                tmp_result += tree[left]
                right -= 1
            
            left >>= 1
            right >>= 1

        return tmp_result
    
    for i in arr :
        final_result += query(i + n - 1, 2*n)
        update(i + n - 1)

    print(final_result)

if __name__ == "__main__" :
    solution()