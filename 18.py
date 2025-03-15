rows = 5
for i in range(rows):
    s = 69 - i  
    for j in range(i + 1):
        print(chr(s + j), end="")
    print()
