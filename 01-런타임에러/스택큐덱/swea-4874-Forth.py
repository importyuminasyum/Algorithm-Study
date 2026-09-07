T = int(input())
for tc in range(1, T+1):
    forth_code = list(input().split())
    result = 0
    stack = []

    for i in range(len(forth_code)):
        if forth_code[i] == '.':
            result = stack.pop()

        if forth_code[i] == '+':
            b = int(stack.pop())
            a = int(stack.pop())

            if a in ('+', '-', '*', '/') or b in ('+', '-', '*', '/'):
                result = 'error'
                break

            stack.append(a + b)
        elif forth_code[i] == '-':
            b = int(stack.pop())
            a = int(stack.pop())
            

            if a in ('+', '-', '*', '/') or b in ('+', '-', '*', '/'):
                result = 'error'
                break

            stack.append(a - b)
        elif forth_code[i] == '*':
            b = int(stack.pop())
            a = int(stack.pop())

            if a in ('+', '-', '*', '/') or b in ('+', '-', '*', '/'):
                result = 'error'
                break

            stack.append(a * b)
        elif forth_code[i] == '/':
            b = int(stack.pop())
            a = int(stack.pop())

            if a in ('+', '-', '*', '/') or b in ('+', '-', '*', '/'):
                result = 'error'
                break

            stack.append(a // b)
  
        else:
            stack.append(forth_code[i])

    print(f'#{tc} {result}')