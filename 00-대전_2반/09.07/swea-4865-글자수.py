T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    count = {}
    for ch in str1:
        count[ch] = 0

    for ch in str2:
        if ch in count:
            count[ch] += 1

    print(max(count.values()))
