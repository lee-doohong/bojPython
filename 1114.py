import sys

L, K, C = map(int, sys.stdin.readline().split())
location = list(set(map(int, sys.stdin.readline().split())))
location.sort(reverse=True)

# L = 길이, K = 자를 수 있는 위치, C = 자를 수 있는 최대 횟수
# print("L = {0}, K = {1}, C = {2}".format(L, K, C))
# print(f"location = {location}")

def main() :
    min_length = 0; first_cut = sys.maxsize
    # 길이가 1인건 가장 잘게 자른거고 
    # 길이가 L인건 한번도 안자른거다.

    start = 1; end = L
    tmp_arr = []
    #binary_search 시작
    while (start < end) :
        mid = (start + end) / 2

        # 가장 작은 min_length를 찾아야 한다.
        # can_cut은 자른 위치들을 반환한다.(가능한경우) 불가능한 경우에는 빈 list를 반환한다.        
        tmp_arr = can_cut(mid)

        if tmp_arr : # 자르는게 성공한 경우 = 더 짧은 최대길이로 잘라본다.
            min_length = mid
            first_cut = tmp_arr[tmp_arr.length - 1]
            end = mid - 1
        else : # 자르는게 실패한 경우 = 더 긴 최대길이로 잘라본다.
            start = mid + 1

    print(f"{min_length} {first_cut}")

# can_cut은 자른 위치들을 반환한다.(가능한경우) 불가능한 경우에는 빈 list를 반환한다.        
def can_cut(length) :
    return_list = []
    now_pos = L
    former_pos = L
    cnt = 0
    for pos in location :
        if (now_pos - pos) <= length :
            former_pos = pos


if __name__ == "__main__" :
    main()