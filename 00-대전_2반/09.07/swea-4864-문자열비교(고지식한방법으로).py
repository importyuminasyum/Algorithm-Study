def brute_force(str1, str2):
    i = 0
    j = 0 
    N, M = len(str1), len(str2)
    count = 0
    while i < N and j < M:
        if str2[j] != str1[i]:
            j += 1
        else:
            count += 1
            j += 1
            i += 1

    if count == N:
        return 1

    return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f'#{tc} {brute_force(str1, str2)}')
