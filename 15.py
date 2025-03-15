rows = 5
for i in range(rows,0,-1):
    pattern = "".join(chr(65+j) for j in range(i))
    print(pattern)
