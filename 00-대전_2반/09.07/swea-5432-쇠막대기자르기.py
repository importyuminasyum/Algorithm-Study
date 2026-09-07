T = int(input())
for tc in range(1, T+1):
    parentheses = input()

    cul_stick_count, result = 0, 0
    for i in range(len(parentheses)):
        if parentheses[i] == '(':
            if parentheses[i+1] == ')':
                result += cul_stick_count
            else:
                cul_stick_count += 1
        elif parentheses[i-1] == ')':
            cul_stick_count -= 1
            result += 1

    print(f'#{tc} {result}')

'''
( 이면
이게 레이저:
    쇠막대기 자르기 
    조각이 지금 쇠막대기 개수만큼 + 됨
이게 그냥 막대기 시작점
    쇠막대기 + 1

) 이면
이게 레이저:
    쇠 막대기 자르기 - 머 안 함
이게 막대기 끝
    쇠막대기 - 1
    조각 + 1
'''
            