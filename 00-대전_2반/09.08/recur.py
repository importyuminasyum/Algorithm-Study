def A(idx):
    if idx == 10:
        return

    print(idx)
    A(idx + 1)

def B(idx):
    if idx == 10:
        return
    
    B(idx + 1)
    print(idx)

a = 0
A(0)
B(0)