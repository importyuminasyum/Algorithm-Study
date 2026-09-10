T = int(input())
for tc in range(1, T+1):
    codes = input()
    stack = []
 
    result = 1
 
    for i in range(len(codes)):
        if codes[i] == '{' or codes[i] == '(':
            stack.append(codes[i])
 
        elif codes[i] == '}':
            if not stack or stack.pop() != '{':
                result = 0
                break
 
        elif codes[i] == ')':
            if not stack or stack.pop() != '(':
                result = 0
                break
 
    if stack:
        result = 0
 
    print(f'#{tc} {result}')