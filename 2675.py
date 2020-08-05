for i in range(int(input())):
    redo, str= input().split(" ")
    for j in str:
        for k in range(int(redo)):
            print(j, end="")
    print()
