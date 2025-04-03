from sys import maxsize
from sys import stdin


test = [1, 3, 5, 10, 11, 13, 14]

def bin_search (lo, hi, target) :
    global test
    while(lo < hi) : 
        mid = int((lo + hi) / 2)
        # 가운데 값보다 target값이 크거나 같으면 
        if (test[mid] < target) :
            lo = mid + 1
        elif (test[mid] > target) :
            hi = mid
        print("lo : {0}, hi : {1}, mid : {3}, target : {2}".format(lo, hi, target, mid))
    
    return hi

print(bin_search(0, len(test) - 1, 7))