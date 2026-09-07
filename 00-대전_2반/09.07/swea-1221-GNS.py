transfer = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for _ in range(1, T+1):
    text, N = input().split()
    N = int(N)
    word = list(input().split())
    idx_list = []

    for i in range(N):
        idx_list.append(transfer.index(word[i]))

    idx_list.sort()

    print(text)
    for i in idx_list:
        print(transfer[i], end=' ')
