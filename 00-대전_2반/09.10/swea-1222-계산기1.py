for tc in range(1, 11):
    N = int(input())
    expression = input()
    operator, stack = [], []
    result = []

    for c in expression:
        if c.isdigit():
            stack.append(c)

        else:
            if operator:
                stack.append(operator.pop())
            operator.append(c)

    while operator:
        stack.append(operator.pop())

    for h in stack:
        if h.isdigit():
            result.append(int(h))

        else:
            if len(result) > 1:
                b = result.pop()
                a = result.pop()
                result.append(a + b)

    print(f'#{tc} {result.pop()}')