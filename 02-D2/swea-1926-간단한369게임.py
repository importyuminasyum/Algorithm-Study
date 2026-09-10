'''
369 게임인데, 숫자가 33 이면 -- 라고 출력해야 함
'''
N = int(input())
numbers = [str(num) for num in range(1, N + 1)]
clap = {'3', '6', '9'}

for idx in range(N):
    count = 0
    for n in numbers[idx]:
        if n in clap:
            count += 1
    if count:
        numbers[idx] = '-' * count

print(' '.join(numbers))
