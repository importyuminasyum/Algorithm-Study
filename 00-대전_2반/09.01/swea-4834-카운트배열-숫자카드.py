T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(input())
    count = [0] * 10

    for a in A:
        count[int(a)] += 1

    index, value = 0, 0
    for c in range(len(count)):
        if count[c] == max(count):
            index, value = c, count[c]

    print(f'#{tc} {index} {value}')