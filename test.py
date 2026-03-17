from sys import stdin

input_val = stdin.read().split()

N = int(input_val[0])

runner =list(map(int, input_val[1:]))
print(f"runner : {runner}")

sorted_runner = sorted([(runner[i], i) for i in range(N)])

for r, (val, original_index) in enumerate(sorted_runner) :
    runner[original_index] = r

print(f"runner : {runner}")


runner = list(map(int, input_val[1:]))

# 기존 등수들을 남겨두고 역량순으로 sort 한다
sorted_runner = sorted([(runner[i], i) for i in range(N)])

# 