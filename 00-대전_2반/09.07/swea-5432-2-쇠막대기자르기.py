T = int(input())
for tc in range(1, T+1):
    parentheses = input()
    stack, result = [], 0
    
    for i in range(len(parentheses)):
        if parentheses[i] == '(':
            stack.append(parentheses[i])

        else:
            pre = stack.pop()

            if parentheses[i - 1] == '(':
                result += len(stack)

            else:
                result += 1

    print(f'#{tc} {result}')

'''
( 이면 스택에 넣기
스택 개수: 현재 활성화된 쇠막대기 개수

다음이 )면 pop
아니면 그냥 둬


) 이면
스택 마지막 봐서 )면 (레이저 아니면)
stack pop
result += 1

'''