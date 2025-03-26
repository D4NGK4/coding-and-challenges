import random

arr = []

for i in range(10):
    arr.append(random.randint(1, 29))

print(arr)

s = arr[0]

for i in range(len(arr)):
    if s < arr[i]:
        s == arr[i]
        print(s)

print(s)
