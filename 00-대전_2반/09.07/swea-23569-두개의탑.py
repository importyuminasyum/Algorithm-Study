'''
두 개의 탑
입력 : T
N, A, B = map(int, input().split())
N: 두 개의 탑을 합친 층 수의 총합
A: A 탑이 차지하고 있는 층의 개수
B: B 탑이 차지하고 있는 층의 개수
N개의 탑을 쌓아올리는 개수
1층에 쌓으면 탑의 비용 = 1 * 주어진 무게

계산
3층 - 그 다음 무거운 거
2층 - 그 다음 무거운 거
1층 - 가장 무거운 거 나열

sort - 7 5 4 3 1
2개씩 끊어서
* 1
* 2
* 3 
합계
'''
T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    blocks = sorted(list(map(int, input().split())))
    result = 0

    # 작은 애 먼저
    if A > B:
        A, B = B, A

    A_count, B_count = A, B

    count = 1
    mul = 1

    while blocks:
        if count <= A:
        # 1층부터 하나씩 pop
            num_a = blocks.pop()
            num_b = blocks.pop()

            result += (num_a + num_b) * mul

            count += 1
            mul += 1

        else:
            num = blocks.pop()
            result += num * mul
            mul += 1
            
    print(f'#{tc} {result}')