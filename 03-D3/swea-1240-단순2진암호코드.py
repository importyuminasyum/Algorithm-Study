# import sys
# sys.stdin = open('input.txt', 'r')
 
code_dict = {'0001101': 0, 
        '0011001': 1, 
        '0010011': 2, 
        '0111101': 3, 
        '0100011': 4, 
        '0110001': 5, 
        '0101111': 6, 
        '0111011': 7, 
        '0110111': 8, 
        '0001011': 9
        }
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    txt = [input() for _ in range(N)]
    code = ''
    for row in txt:
        end = row.rfind('1')
 
        if end != -1:
            code = row[end - 55: end + 1]
            break
 
    # 인덱스: 짝수 합 * 3/ 인덱스: 홀수 == 10의 배수
    even_sum, odd_sum = 0, 0
    for i in range(8):
        num = code_dict[code[7 * i : 7 * (i + 1)]]
 
        if not i % 2:
            odd_sum += num
        else:
            even_sum += num
 
    if not (odd_sum * 3 + even_sum) % 10:
        result = odd_sum + even_sum
 
    else:
        result = 0
 
    print(f'#{tc} {result}')