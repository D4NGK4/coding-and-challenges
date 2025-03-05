key = "the quick brown fox jumps over the lazy dog"
letters = "abcdefghijklmnopqrstuvwxyz"
message = "vkbs bs t suepuv"

seen = set()
result = ""

for i in key:
    if i not in seen:
        if i == " ":
            continue
        seen.add(i)
        result += i

# llool

result = list(result)
letter = list(letters)
ans = []


for i in range(len(message)):
    for j in range(len(result)):
        if message[i] == result[j]:
            ans.append(letter[j])
            break
        if message[i] == " ":
            ans.append(" ")
            break

final = ""
for i in range(len(ans)):
    final += ans[i]

print(final)

print(ans)
