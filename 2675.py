"""
for i in range(int(input())):
    redo, str= input().split(" ")
    for j in str:
        for k in range(int(redo)):
            print(j, end="")
    print()
"""

for i in range(int(input())):
    redo, str = input().split(" ")
    for j in str:
        print(int(redo)*j, end="")
    print()
