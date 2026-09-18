T = int(input())
for tc in range(1, T+1):
    num = float(input())
    result = ''

    while num != 0:
        num *= 2

        if num >= 1:
            result += '1'
            num -= 1
        else:
            result += '0'

        if len(result) > 12:
            result = 'overflow'
            break

    print(f'#{tc} {result}')