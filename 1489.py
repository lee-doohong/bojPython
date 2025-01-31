import sys

N = int(input())

A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
result = 0

for i in range(0, N) :
    if A[i] == 0 : continue
    tmp_j = -1
    for j in range(0, N) :
        if B[j] == 0 : continue
        if (A[i] > B[j]) :  
            tmp_j = j
    if tmp_j != -1 :
        A[i] = 0; B[tmp_j] = 0
        result += 2    

for i in range(0, N) :
    if A[i] == 0 : continue
    for j in range(0, N) :
        if B[j] == 0 : continue
        if A[i] == B[j] : 
            A[i] = 0; B[j] = 0
            result += 1
            break

print(result)
            