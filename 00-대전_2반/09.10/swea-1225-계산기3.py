priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
for tc in range(1, 11):
    N = int(input())
    expression = input()
    operator, stack = [], []
    result = []

    # 소괄호 - 열린 소괄호는 무조건 넣기, 닫힌 소괄호 만나면 operator에서 열린 소괄호 만날 때까지 pop
    # operator.pop()과 지금 표현식에서 볼 연산자와 우선순위 판단해서 더 높은 우선순위를 가진 연산자를 스택에 추가
    # priority = {'+': 1, '-': 1, '*': 2, '/': 2} - priority['+'] 와 priority['-'] 이게 같은지 다른지 확인
    # 같으면 먼저 들어온 operator.pop()이 스택에 들어감

    for ch in expression:
        if ch.isdigit():
            stack.append(ch)
        elif ch == '(':
            operator.append('(')
        elif ch == ')':
            while operator:
                a = operator.pop()
                if a == '(':
                    break
                stack.append(a)
        else:
            if not operator:
                operator.append(ch)
                continue

            while operator:
                a = operator[-1]

                if priority[ch] > priority[a]:
                    break

                stack.append(operator.pop())

            operator.append(ch)

    while operator:
        stack.append(operator.pop())
    print(stack)
    for ch in stack:
        print(result)
        if ch.isdigit():
            result.append(int(ch))
            continue

        if len(result) > 1:
            b = result.pop()
            a = result.pop()

            if ch == '+':
                result.append(a + b)
                
            elif ch == '-':
                result.append(a - b)

            elif ch == '*':
                result.append(a * b)

            else:
                result.append(int(a / b))

    print(f'#{tc} {result.pop()}')