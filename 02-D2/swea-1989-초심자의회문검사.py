t = int(input())
for test_case in range(1, t + 1):
    word = input()
    word_reverse = word[::-1]
    if word == word_reverse:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')