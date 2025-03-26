s = "(()())(())"

s = list(s)
counter = 0
ans = ""

for i in range(len(s)):
    if s[i] == "(":
        if counter > 0:
            ans += "("
        counter += 1
    if s[i] == ")":
        if counter > 1:
            ans += ")"
        counter -= 1

print(ans)


# this is a comment for a daily commit heheheh
# ditto lol
