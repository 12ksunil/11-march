rows = 5
for i in range(1, rows + 1):
    s = ""
    for j in range(i):
        s += chr(65 + j)  
    for j in range(i - 2, -1, -1): 
        s += chr(65 + j)
    print(' '*(rows -i)+ s) 
