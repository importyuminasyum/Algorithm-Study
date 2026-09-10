'''
A를 돌면서 
B 처음 값이랑 똑같으면 pick_A에 넣기
다르면 지나가
i 증가

'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(input().split())
    B = list(input().split())
    pick_A = []
    j = 0
    result = 'NO'

    for i in range(N):
        if j == M:
            break

        if A[i] == B[j]:
            pick_A.append(A[i])
            j += 1

    if pick_A == B:
        result = 'YES'

    print(f'#{tc} {result}')
    