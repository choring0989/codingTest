a = int(input())

for i in range(0, a):
    for j in range(0, a):
        if(j%2 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    for j in range(0, a):
        if(j%2 == 0):
            print(" ", end="")
        else:
            print("*", end="")
    print()
