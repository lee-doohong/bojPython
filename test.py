from sys import maxsize
from sys import stdin

# arr = [1]

# def change_N(n) :
#     n.append(100)

# if __name__ == '__main__' :
#     print(arr)
#     change_N(arr)
#     print(arr)

# 함수안에서도 global을 선언하면 
# 전역 변수를 바꿀수 있다.

# def test_global() :
#     global b 
#     b = [1]

# def test_global2() :
#     return b + 100 

# print(a)
# print(id(a))
# change_N2(a)
# print(a)

# 변수 그 자체를 바꾸는 거면 밖에도 영향을 안미치는데, list 객체 중 일부를 바꾸면 밖에 영향을 미치네?
# print(a)
# test_global2()
# print(a)

# print(b)
# test_global2()
# print(b)

# print(b, id(b))
# change_N2(b)
# print(b)

a = (1,2,)

if 3 in a : print('yes')
else : print('no')

