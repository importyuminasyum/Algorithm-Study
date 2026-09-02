T = int(input())
for tc in range(1, T+1):
    N = int(input())
    names = []
    for _ in range(N):
        names.append(input())

    names = list(set(names))
    print(names)
    for i in range(N - 1):
        min_idx = i

        for j in range(i + 1, N):
            if len(names[j]) < len(names[min_idx]):
                min_idx = j

            elif len(names[j]) == len(names[min_idx]):
                for str in range(len(names[j])):
                    if ord(names[j][str]) < ord(names[min_idx][str]):
                        min_idx = j

        names[i], names[min_idx] = names[min_idx], names[i]

    print(f'#{tc}')
    for name in names:
        print(name)