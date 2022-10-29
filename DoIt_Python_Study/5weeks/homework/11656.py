S = input()

words = []

while S:
    words.append(S)
    S = S[1:]

words.sort()

for word in words:
    print(word)