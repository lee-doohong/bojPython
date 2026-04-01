from sys import stdin
import collections

def solution() :
    #부품은 1~N-1개 까지 있다.
    N = int(stdin.readline())
    M = int(stdin.readline())

    Q = collections.deque()

    # 만드는데 필요한 부속 부품의 수(1부터 N-1까지 있다.)// 부속 부품의 수가 0이 되면 Q에 집어 넣는다. 
    # 입력 끝나고 진입차수(inderee)가 그래도 0인 것들은 기본부품..
    indegree = [0] * (N + 1)
    # adj라고 서로 관계를 나타내는게 필요함
    # adj[기본부품, 또는 부속부품] = [만드는대상, 갯수]
    # 나중에 Q에서 하나꺼내서 adj 돌리면서 // count 부품이 몇개 인지 계산해본다
    adj = [[] for _ in range(N + 1)]
    # count에 다가 필요한 부품 넣으면 되나?
    # count는 결국 해당 부품을 만드는데 필요한 기본 부품이 몇개인지 나타내는 것일 뿐이고
    # 특정부품을 만들면 거기 열을 값을 바꾸면 됨
    # 예를 들어 3번 부품 만드는데 2번 부품이 3개 필요하다 그러면 2번 열을 보고 필요한 갯수를
    # 참고해서 3번 부품 만드는데 기본 부품이 몇개 필요 한지를 계산하는 것이다.
    count = [[0] * (N + 1) for _ in range(N + 1)]

    #입력 데이터 처리
    for _ in range(M) :
        # X 중간부품이나 완제품 번호 // Y 재료부품(중간부품이나 기본부품) // K갯수
        X, Y, K = list(map(int, stdin.readline().split()))
        indegree[X] += 1
        adj[Y].append([X, K])
    
    # 기본부품 넣어두는곳
    basic = [] 
    
    # 기본부품 리스트에도 넣고 Q에도 집어 넣기
    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            Q.append(i)
            basic.append(i)

    #Q에 들어 있는것들 처리
    while Q :
        # Q에 있는거 꺼내서 now 변수에 할당 // now는 재료부품임.
        now = Q.popleft()
        # adj에서 now가 어디어디 들어가야 할지 찾아보기 
        # 여기서 i, j는 [만들어질 부품, now가 몇개 사용되는지]
        for i, j in adj[now] :
            # 각 기본부품 별로 확인
            for b in basic :
                count[i][b] += count[now][b] * j

            indegree[i] -= 1
            if not indegree[i] : Q.append(i)

    # 디버깅
    for c in count :
        print(c)
        
    result = []
    for b in basic :
        result.append(f"{b} {count[N][b]}")
    
    print("\n".join(result))
    return

if __name__ == "__main__" :
    solution()