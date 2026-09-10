T = int(input())
for tc in range(1, T+1):
    forth_code = list(input().split())
    result = 0
    stack = []

    for i in range(len(forth_code) - 1):
        # 받은 수가 숫자일 때 스택에 넣기
        if forth_code[i].isdigit():
            stack.append(int(forth_code[i]))

        elif stack:
            if len(stack) < 2:
                result = 'error'
                break

            else:
                b = stack.pop()
                a = stack.pop()

                if forth_code[i] == '+':
                    stack.append(a + b)
                if forth_code[i] == '-':
                    stack.append(a - b)
                if forth_code[i] == '*':
                    stack.append(a * b)
                if forth_code[i] == '/':
                    stack.append(int(a / b))

    if len(stack) == 1 and result.isdigit():
        result = stack.pop()
    
    print(f'#{tc} {result}')