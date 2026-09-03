T = int(input())
for tc in range(1, T+1):
    parentheses = input()
    count = 0 # 현재 레이저를 만났을 때 쪼갤 수 
    result = 0 # 현재까지 모은 쇠막대기 조각 수

    for idx in range(len(parentheses)):
        if parentheses[idx] == '(':
            if idx + 1 < len(parentheses) and parentheses[idx + 1] == ')':
                result += count
            else:
                count += 1
        else:
            if parentheses[idx - 1] == '(':
                continue
            count -= 1
            result += 1

    print(f'#{tc} {result}')