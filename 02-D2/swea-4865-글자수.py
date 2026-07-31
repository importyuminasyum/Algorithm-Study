T = int(input())

for test_case in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    str_dic = {}

    for str in str1:
        str_dic[str] = 0

    for str in str2:
        if str in str_dic:
            str_dic[str] += 1

    print(f"#{test_case} {max(list(str_dic.values()))}")