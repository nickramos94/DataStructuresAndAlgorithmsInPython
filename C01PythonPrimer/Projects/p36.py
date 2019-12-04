words = input("Enter a space-separated list of words : ").split()
words_count = dict()

for word in words:
    words_count[word] = words_count.get(word, 0) + 1

print()
for word, count in words_count.items():
    print(word, count)
