for i in range(4):
    #alphabet
    for j in range(i + 1):
        print(chr(65 + i +j), end = " ")
    print(" " *3,end=" ")

    #repeated number
    for j in range(4 - i):
        print(4 - i,end=" ")
    print(" ", end=" ")
    
    
