'''
열린 괄호 + 1
닫힌 괄호 - 앞에 값이 열린 괄호면 넘어가
- 아니면 열린 괄호 + 1
'''

T = int(input())
for tc in range(1, T+1):
    S = input()
    ball = 0

    for i in range(len(S)):
        if S[i] == '(':
            ball += 1
            continue

        if S[i] == ')':
            if S[i - 1] == '(':
                continue

            ball += 1

    print(f'#{tc} {ball}')