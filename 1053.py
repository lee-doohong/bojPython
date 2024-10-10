from itertools import combinations
import sys

def DFS(left, right) :
    if (left > right) : return 0
    if DP[left][right] != sys.maxsize : return DP[left][right]
    for i, j in [[0, 1], [1, 0], [1, 1]] :
        DFS(left + i, right - j)
        DP[left][right] = min(DP(left + i, right + j) + int(not(i and j and seq[left] == seq[right])), DP[left][right])

def DPinit() :
    global DP
    DP = [[int(i<j) * sys.maxsize for j in range(N)] for i in range(N)]

seq = [*input()]
N = len(seq)

DPinit()

answer = DFS(0, N-1)

for i, j in combinations(range(N), 2) : 
    if (seq[i] == seq[j]) : continue
    seq[i], seq[j] = seq[j], seq[i]
    DPinit()
    answer = min(answer, DFS(0, N-1) + 1)
    seq[j], seq[i] = seq[i], seq[j]


print(answer)