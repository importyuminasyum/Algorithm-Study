T = int(input())
for _ in range(1, T+1):
    t = int(input())
    scores = list(map(int, input().split()))
    count = [0] * (max(scores) + 1)
    for score in scores:
        count[score] += 1
    print(f'#{t} {max(range(len(count)), key=lambda i:(count[i], i))}')