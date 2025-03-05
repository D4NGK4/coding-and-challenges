s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

s = list(s)

dictionary = {}


for i in range(len(indices)):
    item = {s[i]: indices[i]}
    dictionary.append(item)
