'''
길이가 N인 문자열 안에 길이가 M인 회문이 있으면 그 회문 출력, 회문이 없으면 NONE 출력
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    text = input()
    result = 'NONE'
    #문자열 슬라이싱할 거임
    for i in range(N - M + 1):
        slicing_text = text[i:i+M]
        if slicing_text == slicing_text[::-1]:
            result = slicing_text
    print(f'#{tc} {result}')