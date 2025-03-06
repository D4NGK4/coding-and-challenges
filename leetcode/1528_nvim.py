s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

t = len(indices)
ans = ""
s = list(s)

for i in range(t):
    for j in range(len(indices)):
        if i == indices[j]:
            ans += s[j]

print(ans)
