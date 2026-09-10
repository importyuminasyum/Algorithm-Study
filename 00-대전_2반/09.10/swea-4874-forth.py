T = int(input())
for tc in range(1, T+1):
    expression = list(input().split())
    stack = []
    result = 1
    
    for ch in expression:
        if ch == '.':
            break

        if ch.isdigit():
            stack.append(ch)

        else:
            if len(stack) > 1:
                b = int(stack.pop())
                a = int(stack.pop())

                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

            else:
                result = 0
                break

    if len(stack) == 1 and result:
        result = stack.pop()
    else:
        result = 'error'

    print(f'#{tc} {result}')