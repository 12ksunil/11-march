rows = 5
for i in range(1, rows + 1):
    pattern = "".join(str((i+j) % 2) for j in range(i))
    print(pattern)