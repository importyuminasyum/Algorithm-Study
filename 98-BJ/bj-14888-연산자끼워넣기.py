def calculate(a, b, op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b 
    if op == 2:
        return a * b
    if op == 3:
        if a < 0:
            return -((-a) // b)
        return a // b

def dfs(idx, value):
    global min_val, max_val

    if idx == N:
        min_val = min(min_val, value)
        max_val = max(max_val, value)
        return
    
    for op in range(4):
        if operator[op]:
            operator[op] -= 1

            next_value = calculate(value, A[idx], op)
            dfs(idx + 1, next_value)

            operator[op] += 1
            
N = int(input())
A = list(map(int, input().split()))

# +(0), -(1), *(2), //(3)
operator = list(map(int, input().split()))

max_val, min_val = float('-inf'), float('inf')

dfs(1, A[0])
print(max_val)
print(min_val)