from sys import stdin
import sys

def solution() :
   input_data = stdin.read().split()
   if not input_data :
      return
   
   N = int(input_data[0])
   tree = [0] * N * 2

   runners = list(map(int, input_data[1:]))
   # 각 러너들의 기존 순위를 매긴 다음 달리기 역량 순으로 솔팅..
   sorted_runners = sorted([(runners[i], i) for i in range(N)])
   # r 솔팅한 순위.. 역량 낮은 선수 부터 높은 선수 순... 
   # runner[기존위치..] = 솔팅순위
   # 기존 역량 val은 필요 없다.
   for r, (val, original_index) in enumerate(sorted_runners) :
      runners[original_index]  = r

   # 부모채우기
   def update(index) :
      tree[index] = 1
      
      while 1:
         if not index // 2 : return
         tree[index // 2] = tree[index] + tree[index ^ 1]
         index //= 2

   def query(left, right) :
      result = 0

      while left <= right :
      # left가 홀수면 더하고 오른쪽으로 넘어가고(+1), right가 짝수면 더하고 왼쪽으로 넘어간다(-1)
         if left & 1 :
            result += tree[left]
            left += 1 
         if not (right & 1) :
            result += tree[right]
            right -= 1

         left //= 2
         right //= 2
         
      return result  

   enable_overtake_num = []
   result = []

   for i in runners :
      enable_overtake_num.append(query(N, i + N - 1))
      update(i + N)
   
   for i in range(N) :
      tmp_rank = i + 1 - enable_overtake_num[i]
      result.append(str(tmp_rank))

   sys.stdout.write("\n".join(result))
 
if __name__ == "__main__" :
   solution()