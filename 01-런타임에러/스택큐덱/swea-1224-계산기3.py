for tc in range(1, 11):
    N = int(input())
    expression = input()
    stack = []
    result = 0
    i = 0

    while i < N:
        # 괄호를 만나면 다음 괄호가 나올 떄까지 그 안 연산을 수행해야 함
        if expression[i] == '(':
            stack.append(expression[i])

        if expression[i] == ')':
            

        # 숫자 만나면 스택에 넣기
        if expression[i].isdigit():
            stack.append(int(expression[i]))

        # 연산자 만나면 다음 거랑 스택 젤 최근 거 연산해서 스택에 넣기
        else:
            if stack and expression[i] == '*':
                stack.append(stack.pop() * int(expression[i + 1]))
                i += 1

        i += 1

    result = sum(stack)

    print(f'#{tc} {result}')

    9 11
    9 ( 10 1 )
    일단 숫자 넣고
    ( 보이면 넣고
     숫자 넣고
    ) 나오면 stack.pop() == '('