'''
숫자열 A, B 
- 길이가 짧은 애가 긴 애 돌아야 함
N: A 긴
M: B
if N > M:
    N, M = M, N
    A, B = B, A


마주보는 숫자들 곱해서 더할 떄의 최댓값
그럼 갱신해
max_sum_mul = 0

# 이건 큰 배열의 첫번째 기준 인덱스임
5 3 
0 1 2 3 4 

0 1 2 
0 1 2
1 2 3
0 1 2 
2 3 4
0 1 2 

0 0 
0 1 
0 2 
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N < M:
        N, M = M, N
        A, B = B, A

    max_mul_sum = 0

    for i in range(N - M + 1):
        temp_mul_sum = 0

        for j in range(M):
            temp_mul_sum += A[i + j] * B[j]

        max_mul_sum = max(max_mul_sum, temp_mul_sum)

    print(f'#{tc} {max_mul_sum}')
