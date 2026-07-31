t = int(input())

for s in range(1,t+1):
    n = input()
    cnt = 0
    for i in range(1, len(n)):
        if n[0] != 'a':
            cnt = 0
            break
        else:
            if ord(n[i])-ord(n[i-1]) == 1:
                cnt += 1
            else:
                break
    print(f'#{s} {cnt}')