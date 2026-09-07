for tc in range(1, 11):
    N = int(input())
    expression = input()
    stack = []
    result = 0
    i = 0

    while i < N - 1:
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