'''
현재 인덱스에서부터 다음 거의 상태를 다 바꾸는 함수
0 0 0
0 1 1
0 1 0

1 1 1 1 1 0 0 0 1 1
앞 인덱스부터 정답과 비교하기 - 같으면 냅둬
인덱스 2번에서 달라? 그러면 거기서부터 뒤까지 반복하면서 바꾸기
카운트 증가
또 정답과 비교하기 - 같으면 냅둬
1 1 0 0 0 1 1 1 0 0
1 1 0 1 1 0 0 0 1 1
1 1 0 1 1 0 1 1 0 0

1 1 0 1 1 0 1 1 0 0

dict = {0:1, 1:0}

for idx in range(N):
    if prev[idx] == next[idx]:
        continue
    
    for i in range(idx, N):
        prev[i] = dict[prev[i]]

    count += 1
'''
dict = {0:1, 1:0}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prev = list(map(int, input().split()))
    next = list(map(int, input().split()))
    count = 0

    for idx in range(N):
        if prev[idx] == next[idx]:
            continue
        
        for i in range(idx, N):
            prev[i] = dict[prev[i]]

        count += 1

    print(f'#{tc} {count}')