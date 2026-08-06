def check(sentences):
    stack = []
    for word in sentences:
        if word == '(' or word == '{':
            stack.append(word)

        elif word == ')' or word == '}':
            if not stack:
                return 0
            elif (word == ')' and stack[-1] == '(') or (word == '{' and stack[-1] == '{'):
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    
    return 1

T = int(input())
for tc in range(1, T + 1):
    sentences = input()

    print(f'#{tc} {check(sentences)}')