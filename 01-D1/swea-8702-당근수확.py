'''
N
10개 이하의 당근 개수 배열

1번부터 연속으로 두 개의 배열로 나눴을 때
그 때의 수확한 당근의 개수의 차이가 최소가 되도록 하는 방법

인덱스: 첫 일꾼의 마지막 영역, 값: 수확 개수의 차를 담을 리스트
N = 5 일때 가능한 경우
0 1 2 3 4
1/4
2/3
3/2
4/1
N - 1 개


출력: 첫 일꾼의 마지막 영역 / 최소 수확 개수의 차이
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = list(map(int, input().split()))
    min_diff, min_num = float('inf'), 0

    for idx in range(1, N - 1):
        diff = abs(sum(area[:idx]) - sum(area[idx:]))
        if diff < min_diff:
            min_diff = diff
            min_num = idx
        
    print(f'#{tc} {min_num} {min_diff}')