Vowels = ["A","E","I","O","U"]

word = input("Enter a word: ")
word = word.upper()

for i in range(0, len(word)):
    if word[i] not in Vowels:
        print(word[i], end="" )
    else:
        continue