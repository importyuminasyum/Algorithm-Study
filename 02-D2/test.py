arr = 'CAAABBA'

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        print(i, i+1)
        new_arr = arr[:i] + arr[i + 2:]
        
print(new_arr)