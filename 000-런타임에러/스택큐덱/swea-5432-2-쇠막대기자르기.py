T = int(input())
for tc in range(1, T+1):
    parentheses = input()
    stack = []
    count = 0 # 현재 레이저를 만났을 때 쪼갤 수 
    result = 0 # 현재까지 모은 쇠막대기 조각 수

    # 괄호 하나 검사
    # ( 이고 
    # 다음 거가 )면 pop 하고 스택 길이 result에 넣기 - 레이저 한 거임
    # 다음 거가 (면 그냥 스택에 넣기
    # ) 이고
    # 레이저 아니면 pop하고 result에 하나 추가하기 
    
    for idx in range(len(parentheses)):
        if parentheses[idx] == '(':
            stack.append(parentheses[idx])
            if idx < len(parentheses) - 1 and parentheses[idx + 1] == ')':
                stack.pop()
                result += len(stack)
        else:
            if parentheses[idx - 1] == ')':
                stack.pop()
                result += 1

    print(f'#{tc} {result}')