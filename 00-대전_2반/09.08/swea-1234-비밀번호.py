for tc in range(1, 11):
    N, numbers = input().split()
    N = int(N)
    numbers = list(map(int, numbers))
    stack = [numbers[0], ]
 
    for i in range(1, N):
 
        if stack and (numbers[i] == stack[-1]):
            stack.pop()
 
        else:
            stack.append(numbers[i])
 
    print(f"#{tc} {''.join(map(str, stack))}")