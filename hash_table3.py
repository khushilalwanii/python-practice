with open("poem.txt", "r") as f:
    text = f.read()

text = text.replace(',', '').replace('.', '').replace(';','').replace('\n', ' ').lower()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word} : {count}")


counter = 1
for word, count in word_count.items():
    print(f"{counter}. {word} : {count}")
    counter += 1
