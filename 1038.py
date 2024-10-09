from itertools import combinations
import sys

finalList = []
for i in range(1, 11) :
    for j in combinations(range(10), i) :
            finalList.append(int(''.join(map(lambda x:str(x), sorted(list(j), reverse=True)))))

finalList.sort()

N = int(sys.stdin.readline())

if (len(finalList) > N) :
    print(finalList[N])
else : 
    print(-1)