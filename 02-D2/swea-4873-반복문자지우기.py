def eraser(repeat_word):
    stack = []
    for i in range(len(repeat_word)):    
        if stack and repeat_word[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(repeat_word[i])
    return len(stack)
 
T = int(input())
for tc in range(1, T + 1):
    repeat_word = input()
    print(f'#{tc} {eraser(repeat_word)}')