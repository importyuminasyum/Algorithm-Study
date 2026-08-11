T = int(input())
for tc in range(1, T + 1):
    brackets = list(input())

    for i in range(len(brackets) - 1):
        if brackets[i] == '(' and brackets[i + 1] == ')':
            checkpoint = i + 1

        
