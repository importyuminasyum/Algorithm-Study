for _ in range(1, 11):
    tc = int(input())
    ladder = [
        list(map(int, input().split()))
        for _ in range(100)
    ]
    result = []
    for start_c in range(100):
        if not ladder[99][start_c]:
            continue

        r, c = 99, start_c
        temp_count = 0

        while r > 0:
            if c > 0 and ladder[r][c - 1]:  
                while c > 0 and ladder[r][c - 1]:
                    c -= 1
                    temp_count += 1
            elif c < 99 and ladder[r][c + 1]:
                while c < 99 and ladder[r][c + 1]:
                    c += 1
                    temp_count += 1
            r -= 1
            temp_count += 1

        result.append((temp_count, c))

    print(f'#{tc} {min(result, key=lambda x: (x[0], -x[1]))[1]}')
