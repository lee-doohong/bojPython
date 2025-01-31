from sys import stdin

# 일단 input 부터 짜자..

W, H = list(map(int, stdin.readline().split(" ")))

print(W)
print(H)

N = int(input())

class Extent :
    def __init__ (self, a) :
        self.a = a[0]
        self.b = a[1]
        self.c = a[0] * a[1]
    
    def __str__ (self) :
        return (f'w1 : {self.a}, h1: {self.b} ')

extents = sorted([Extent(list(map(int, stdin.readline().split(" ")))) for _ in range(N)], key = lambda extent: extent.c, reverse=True)

for e in extents :
    print(e)

print(extents)


    