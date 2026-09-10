for tc in range(1, 11):
    N = int(input())
    expression = input()
    value, operator = [], []
    result = 0
    i = 0

    while i < N:
        # 괄호를 만나면 다음 괄호가 나올 떄까지 그 안 연산을 수행해야 함
        if expression[i].isdigit():
            value.append(int(expression[i]))

        elif expression[i] == '*' or expression[i] == '+':  
            operator.append(expression[i])

        elif expression[i] == '(':
            operator.append('(')
            
        else:
            while value and operator:
                b = value.pop()
                a = value.pop()

                if operator.pop() == '(':
                    break

                if operator.pop() == '*':
                    value.append(a * b)

                if operator.pop() == '+':
                    value.append(a + b)

                i += 1

        i += 1 

    i = 0

    while i < len(value):    
        b = value.pop()
        a = value.pop()

        if operator.pop() == ')':
            break

        if operator.pop() == '*':
            value.append(a * b)

        if operator.pop() == '+':
            value.append(a + b)

        i += 1

    print(f'#{tc} {result}')