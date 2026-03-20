from sys import stdin

def solution() :
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    tree = [0] * 2 * n
    final_result = 0

    def update(index) :
        # print(f"[update] index {index}")
        tree[index] = 1
        while 1 :
            if not index >> 1 :
                return
            else :
                tree[index >> 1] = tree[index] + tree[index ^ 1]
                index >>= 1
    
    # 나보다 큰게 이미 등록되어 있다는것 ? -> 인버스라는것.
    def query(left, right) : # left는 포함하고 right는 포함하지 않는 식으로 만들어 보자.
        # print(f"left {left} right {right}")
        tmp_result = 0
        while left <= right : # left가 짝수면 그냥 올라가고 // 홀수면 더하고 오른쪽으로 가야 한다
                            # righ가 홀수면 그냥 올라가고 // 짝수면 더하고 왼쪽으로 가야 한다
            if left & 1 : # left가 홀수면 아래 연산을 실행해야 한다.
                tmp_result += tree[left]
                left += 1
            if not (right & 1) : # right가 짝수면 아래 연산을 실행해야 한다.
                tmp_result += tree[right]
                right -= 1
            
            left >>= 1
            right >>= 1

        return tmp_result
    
    for i in range(len(arr)) : # 이렇게 하면 range는 i는 0부터 n - 1이 된다.
        # print(f"[for] before_tree : {tree}, need to process : {arr[i]} ")
        final_result += query(arr[i] - 1 + n, n * 2 - 1) # 원래 arr은 
        update(arr[i] - 1 + n)
        # print(f"[for] after tree : {tree}")
    print(final_result)

if __name__ == "__main__" :
    solution()