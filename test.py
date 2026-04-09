import copy

a = [[0] * 3] * 3
b = [[0] * 3 for _ in range(3)]

a[0][0] = 1
print(a)
print(b)