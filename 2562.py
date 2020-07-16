
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
max = 0
index = -1

for i in range(len(arr)):
   arr[i] = int(input())

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        index = i

print(max)
print(index+1)
