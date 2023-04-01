import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for _ in range(int(input())):

    def recur(a):  
        if result[a] != None: return -1 # 방문한 적이 있는지 확인

        if a in dictionary: return a    # 방문한 원소면 그 원소 리턴
        else:
            dictionary[a] = True            # 방문표시
            firstElementInCycle = recur(f[a])
            if firstElementInCycle == -1:   # cycle이 없을경우
                result[a] = False           # a가 팀이 없음을 표시
                return -1
            else:
                result[a] = True
                if a == firstElementInCycle: return -1  # 처음으로 돌아오면 종료
                else: return firstElementInCycle        # 첫 원소 리턴 

    n = int(input())
    f = list(map(int, input().split()))
    f.insert(0, 0)
    elements = [i for i in range(n+1)]  # index를 담고있는 배열
    result = [None for _ in range(n+1)]
    
    dictionary = {}
    for e in elements:
        dictionary.clear()
        recur(e)

    ans = result.count(False)   # 팀 없는 사람들의 합
      
    print(ans)

