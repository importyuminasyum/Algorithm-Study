'''
3 1 4 5 5 
- 무게 분류
- 기준이 되는 k 값
- 분류한 리스트의 최대 최소 길이의 차이가 최소가 되도록
조건을 만족하는 분류 방법이 없다면 -1 출력
모든 무게가 동일하면 세 등급으로 나눌 수 없음
이런 경우에 충족 불가
그러면 len(set(list)) < 3이면은 안되네
1 3 4 5 5 
무게 정렬부터

투 포인터 써야 할 것 같은디

하나 하나 셋
하나 둘 둘

0 1 2 3 4
인덱스 값을 가지고 left right 해가지고
left = 0
right = 1

left = 1
while right:
    for i in range(left + 1, N - 1):
        right = i
        A1, A2, A3 = arr[:left], arr[left:right], arr[right:]

        if len(set(A1) & set(A2)) or len(set(A2) & set(A3)):
            continue

    left += 1

'''

def in_range(n):
    return lo <= n <= hi

T = int(input())
for tc in range(1, T+1):
    N, lo, hi = map(int, input().split())
    weights = list(map(int, input().split()))
    min_diff = float('inf')

    if len(set(weights)) < 3:
        min_diff = -1

    weights.sort()

    left = 1
    while min_diff > -1 and left != N:
        for i in range(left + 1, N):
            right = i
            if weights[left - 1] == weights[left]:
                continue
            
            if weights[right - 1] == weights[right]:
                continue
            
            a, b, c = weights[:left], weights[left:right], weights[right:]
            la, lb, lc = len(a), len(b), len(c)

            if not in_range(la) or not in_range(lb) or not in_range(lc):
                continue

            # if len(set(a) & set(b)) or len(set(b) & set(c)):
            #     continue

            min_diff = min(min_diff, max(la, lb, lc) - min(la, lb, lc))

        left += 1

    if min_diff == float('inf'):
        min_diff = -1

    print(f'#{tc} {min_diff}')
