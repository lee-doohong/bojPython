import sys

def main() :
    N, M = readL()

    quotient, remainder = divmod(N, 6)

    cheap_six = sys.maxsize
    cheap_one = sys.maxsize

    for _ in range(M) : 
        tmp_six, tmp_one = readL()
        cheap_six = min(cheap_six, tmp_six)
        cheap_one = min(cheap_one, tmp_one)

    if (cheap_one * 6 <= cheap_six) : print(N * cheap_one)
    else : 
        print(cheap_six * quotient + min(remainder * cheap_one, cheap_six))



def readL() : 
    return map(int, sys.stdin.readline().split())

if __name__ == "__main__" :
    main()