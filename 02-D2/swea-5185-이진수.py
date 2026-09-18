T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    N = int(N)
    print(f'#{tc} {bin(int(hex_num, 16))[2:].zfill(len(hex_num) * 4)}')