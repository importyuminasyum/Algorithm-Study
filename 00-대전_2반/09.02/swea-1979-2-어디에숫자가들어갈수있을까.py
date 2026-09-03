def count_word(arr, K):
    result = 0 # 누적 개수

    for row in arr:
        count = 0 # 현재 행에서 들어갈 수 있는 칸의 개수
        for x in row:
            if x == '1':
                count += 1
                continue

            if count == K:
                result += 1
            count = 0

        if count == K:
            result += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    puzzle = [
        list(input().split())
        for _ in range(N)
    ]

    print(f'#{tc} {count_word(puzzle, K) + count_word(list(zip(*puzzle)), K)}') 
    
    