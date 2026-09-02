dictionary = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())
for tc in range(1, T+1):
    num, N = input().split()
    words = list(input().split())
    words_index = []

    for word in range(int(N)):
        words_index.append(dictionary[word])

    words_index.sort()

    for idx in words_index:
        sorted_words = [k for k, v in dictionary.items() if v == idx]

    print(num)
    print(sorted_words)