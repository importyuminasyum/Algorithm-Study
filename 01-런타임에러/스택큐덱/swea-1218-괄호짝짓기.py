dictionary = {')': '(', ']': '[', '}': '{', '>': '<'}

for tc in range(1, 11):
    N = int(input())
    parentheses = input()
    stack = []
    result = 1

    for i in range(N):
        # 여는 괄호 만나면 스택에 넣기
        if parentheses[i] in dictionary.values():
            stack.append(parentheses[i])
        # 닫는 괄호 만나면 가장 최근에 스택에 넣은 열린 괄호와 짝이 맞는지 확인
        else:
            if not stack:
                result = 0
                break

            if parentheses[i] in dictionary.keys():
                if stack.pop() != dictionary[parentheses[i]]:
                    result = 0
                    break

    if stack:
        result = 0

    print(f'#{tc} {result}')