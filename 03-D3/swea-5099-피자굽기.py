'''
피자를 순서대로 화덕에 넣을 때, 
화덕에 가장 마지막까지 남아 있는 피자 번호

while oven:
화덕 큐에 N개의 피자를 넣기
화덕 큐에서 처음 거 꺼내기
치즈 양 반으로 줄이고, 0이면 뒤에 다음 피자 넣기
0 아니면 뒤에 다시 넣기
'''
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = deque(list(map(int, input().split())))
    pizza = deque(list(i for i in range(N, M)))
    oven = deque(list(i for i in range(N)))

    while oven:
        check_pizza = oven.popleft()
        if not C[check_pizza] // 2:
            C[check_pizza] //= 2
            if pizza:
                oven.append(pizza.popleft())
            continue

        C[check_pizza] //= 2
        oven.append(check_pizza)

    print(f'#{tc} {check_pizza + 1}')
    