n = int(input())
words = set()
for _ in range(n):
    word = input()
    words.add(word)
words = sorted(words, key=lambda x: (len(x), x))

for w in words:
    print(w)