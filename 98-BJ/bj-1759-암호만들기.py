# 정렬하기 - 조합
# dfs(depth, idx)
# 현재 idx 이후의 문자 중에서 골라서 암호를 완성한다.

# .sort() 하고 시작
vowels = {'a', 'e', 'i', 'o', 'u'}

def dfs(depth, idx):
    if depth == L:
        vowel_count = sum(ch in vowels for ch in pick_password)
        consonant_count = L - vowel_count

        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(pick_password))
        return

    for i in range(idx, len(password)):
        pick_password.append(password[i])
        dfs(depth + 1, i + 1)
        pick_password.pop()

L, C = map(int, input().split())
password = list(input().split())
password.sort()

pick_password = []

dfs(0, 0)