T = int(input())
for tc in range(1, T+1):
    field = list(input())
    count = 0

    for i in range(len(field)-1):
        if field[i] == '(' and field[i + 1] == ')':
            count += 1
            field[i] = '.'
            field[i + 1] = '.'

    for i in range(len(field)):
        if field[i] == '(':
            count += 1
        
        elif field[i] == ')':
            count += 1

    print(f'#{tc}', count)