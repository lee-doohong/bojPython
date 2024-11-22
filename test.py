from sys import maxsize
from sys import stdin

bit = 0b001100
print (bin(bit | 0b11 | 0b110000))
#*은 이미 받은 것을 자르는 개념이네...
#map을 돌리고 나면 그건 그냥 map 객체일 뿐이지 그 이상 뭐가 되는 건 아니다
#다시 list로 활용하려면 list()로 캐스팅 해줘야 ㅎ나다.
#근데 또 숫자 배당은 된다. 이건 그냥 기능인듯..
#파이썬은 그냥 알아서 해주는게 너무 많아서.... 당연히 이것도 되겠지 했다가 안되는게 너무 많음