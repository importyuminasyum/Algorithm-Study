'''
N개의 나무, 각 나무의 키

첫날 + 1
둘째날 + 2

홀수 번째 날: + 1
짝수 번째 날: + 2

모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜 수
- 어떤 날에는 물을 주지 않아도 됨

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    diff = []
    goal = max(trees)
    for i in range(N):
        if trees[i] == goal:
            continue
        diff.append(goal - trees[i])

    day1, day2 = 0, 0
    for d in diff:
        day1 += d % 2
        day2 += d // 2

    while day2 > day1 + 1:
        day1 += 2
        day2 -= 1

    answer = max(day1 * 2 - 1, day2 * 2)

    print(f'#{tc} {answer}')