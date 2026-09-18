import sys
sys.stdin = open('input.txt', 'r')

code_dict = {
    '211': '0', 
    '221': '1', 
    '122': '2', 
    '411': '3', 
    '132': '4', 
    '231': '5', 
    '114': '6', 
    '312': '7', 
    '213': '8', 
    '112': '9'
    }

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    txt = [input() for _ in range(N)]
    check = set()
    final_result = 0

    for row in txt:
        binary = ''

        for x in row:
            binary += format(int(x, 16), '04b')

        c = len(binary) - 1

        while c >= 0:
            if binary[c] == '0':
                c -= 1
                continue

            result = ''

            for _ in range(8):
                c1, c2, c3 = 0, 0, 0
                while c >= 0 and binary[c] == '1':
                    c3 += 1
                    c -= 1

                while c >= 0 and binary[c] == '0':
                    c2 += 1
                    c -= 1

                while c >= 0 and binary[c] == '1':
                    c1 += 1
                    c -= 1
                
                divisor = min(c1, c2, c3)

                c1 //= divisor
                c2 //= divisor
                c3 //= divisor

                ratio = str(c1) + str(c2) + str(c3)

                result = code_dict[ratio] + result

                while c >= 0 and binary[c] == '0':
                    c -= 1

            if result in check:
                continue

            check.add(result)

            nums = list(map(int, result))

            odd_sum = nums[0] + nums[2] + nums[4] + nums[6]
            even_sum = nums[1] + nums[3] + nums[5]
            valid_num = nums[7]

            if not (odd_sum * 3 + even_sum + valid_num) % 10:
                final_result += sum(nums)

    print(f'#{tc} {final_result}')