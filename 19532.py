import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

# print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")

#브루트포스로 푸는 문제임
#단순하게 생각해서는 둘다 만족 하는 x, y 찾으며 그만이다.
flag = False

for x in range (-999, 1000) :
    for y in range (-999, 1000) :
        # print(f"x = {x} y = {y}")
        if ((a * x + b * y) == c) and ((d * x + e * y) == f) :
            print (f"{x} {y}")
            flag = True
            break
    if (flag) :
        break


