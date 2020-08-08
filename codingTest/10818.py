
n = input()
arr = input()

arr = arr.split()
arr = [int(i) for i in arr]

max = -1000000
min = 1000000

for i in range(int(n)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print(min)
print(max)
        
