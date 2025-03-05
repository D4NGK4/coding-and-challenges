key = "the quick brown fox jumps over the lazy dog"
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

print(result)
