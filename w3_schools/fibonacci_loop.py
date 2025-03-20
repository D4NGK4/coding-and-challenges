a = 0
b = 1

c = 0
r = 10

for i in range(r):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
