print()
print("I4GxZuriTrainning: Counting Words")
print("This program counts the number of alphabet in a given word")
print()
word = input("Enter word: ")
um = 0
char = len(word)
for x in range(char):
    um += 1
print("The number of alphabets in the ", word, "is", um)