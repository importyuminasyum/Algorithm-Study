'''
N개의 피자를 동시에 구울 수 있는 화덕에서 
M개의 피자를 순서대로 화덕에 넣을 때, 치즈에 양에 따라 녹는 시간이 달라 꺼내지는 순서가 바뀔 수 있다.
화덕에 가장 마지막까지 남아있는 피자 번호 출력

피자는 1번에서 넣고 빼기 가능
피자받침이 회전, 1번에서 치즈 확인 후 같은 자리 넣기 가능 - 덱?
M개의 피자에 치즈 양이 주어짐
화덕을 한 바퀴 돌 때 - 녹지 않은 치즈의 양은 반으로 줄어듦
치즈가 0이 되면 화덕에서 꺼내고, 그 자리에 남은 피자를 순서대로 넣기

T
N, M - 화덕 크기 / 피자 개수 M
C - M개의 피자에 뿌려진 피즈의 양
'''
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Cheese = list(map(int, input().split()))
    whole_pizza = deque()
    for i in range(1, M + 1):
        whole_pizza.append([i, Cheese[i - 1]])

    melted_pizza, oven_pizza = [], deque()
    for i in range(N):
        oven_pizza.append(whole_pizza.popleft())

    while oven_pizza:
        pizza = oven_pizza.popleft()

        pizza[1] //= 2

        if pizza[1] == 0:
            melted_pizza.append(pizza)

            if whole_pizza:
                oven_pizza.append(whole_pizza.popleft())

        else:
            oven_pizza.append(pizza)

    print(f'#{tc} {melted_pizza[-1][0]}')
    

