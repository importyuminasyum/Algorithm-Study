alpabet = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'khoor'

for step in range(1, 26):
    decoded = list(map(ord, cipher))

    for i in range(len(decoded)):
        decoded[i] += step

        if decoded[i] > ord('z'):
            decoded[i] -= 26

    decoded = list(map(chr, decoded))
    print(''.join(decoded))