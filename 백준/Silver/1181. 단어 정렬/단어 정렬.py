n = int(input())
word_list = []
for _ in range(n):
    word = input()
    if word not in word_list:
        word_list.append(word)
word_list.sort(key=lambda x: (len(x), x))

for w in word_list:
    print(w)