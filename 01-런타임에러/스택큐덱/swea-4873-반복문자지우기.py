T = int(input())
for tc in range(1, T+1):
    words = input()
    stack = []

    for i in range(len(words)):
        stack.append(words[i])

        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    print(f'#{tc} {len(stack)}')