output = set()

for i in range(10):
    temp = int(input())
    output.add(temp%42)

print(len(output))
