#풀이 (파리퇴치와 로직이 동일한 문제이나 이 문제는 가로 검사 할 때와 세로 검사할 때 시작점이 다름)
T = 10

for tc in range(1, T+1):
    M = int(input())    
    graph = [input() for _ in range(8)]  #2차원 리스트를 받을 때 graph로 표현하심
    answer = 0

    for r in range(8):
        for c in range(8-M+1):    #이렇게 적으면 가로검사 시 원하는 시작점 정할 수 있음

            for i in range(M//2):
                if graph[r][c+i] != graph[r][c+M-1-i]:  #이렇게 적으면 M을 2로 나눈 만큼 앞 뒤로 비교 가능
                    break
            else:
                answer += 1         #여기까지 행을 검사한 것. 같은 방식으로 열도 검사

    print(answer)
    for r in range(8-M+1):
        for c in range(8):    

            for i in range(M//2):
                if graph[r+i][c] != graph[r+M-1-i][c]:
                    break
            else:
                answer += 1

    print(f'#{tc} {answer}')         