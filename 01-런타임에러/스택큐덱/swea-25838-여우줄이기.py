def remove_fox(word):
    stack = []
    for ch in word:
        stack.append(ch)
        if len(stack) >= 3:
            if stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
                stack.pop()
                stack.pop()
                stack.pop()
    return stack

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    in_fox_word = list(input())

    print(len(remove_fox(in_fox_word)))
