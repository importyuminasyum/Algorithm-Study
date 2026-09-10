def tournament(deck_a, deck_b):
    global final_winner

    # 어떤 두 배열을 받아서 각각을 둘로 나누기
    # 만약에 길이가 하나면 두 배열 중 이긴 애 인덱스 번호 + 1을 return 해




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    final_winner = N + 1 # 우승자의 번호
    # 0, 1, 2 - 1번 2번 3번

    tournament(cards[:N//2], cards[N//2:N])

    print(f'#{tc} {final_winner}')