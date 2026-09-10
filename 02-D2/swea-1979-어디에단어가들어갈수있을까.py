'''
행 탐색
열 탐색
하면서 정확히 연속된 부분의 길이가 K여야 count += 1
A = [list(input().split()) for _ in range(N)]
AT = list(zip(*arr))

반복문으로 순회하면서 N - K + 1
for r in range(N):
    for c in range(N):
        
'0'을 만나면 
지금까지 count가 K면 결과 + 1
count 초기화

'1'을 만났을 떄 count + 1

그 행이 끝났을 때 한 번 더 검사
'''
def check(array):
    global result 

    for r in range(N):
        count = 0
        for c in range(N):
            if array[r][c] == '0':
                if count == K:
                    result += 1

                count = 0
                continue
            
            count += 1

        if count == K:
            result += 1

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [list(input().split()) for _ in range(N)]
    AT = list(zip(*A))
    result = 0

    check(A)
    check(AT)

    print(f'#{tc} {result}')