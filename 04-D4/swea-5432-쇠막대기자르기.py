T = int(input())
for tc in range(1, T+1):
    result = 0 # 총 조각 수
    count = 0 # 현재 겹쳐있는 막대 수
    field = input()

    for i in range(len(field)):
        if field[i] == '(':
            count += 1
        if field[i] == ')':
            if field[i-1] == '(':
                count -= 1
                result += count
            else:
                count -= 1
                result += 1

    print(f'#{tc} {result}')